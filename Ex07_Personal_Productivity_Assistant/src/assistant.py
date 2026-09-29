"""Personal productivity assistant (offline rule-based core; LLM optional)."""
import json, os, re, random
from datetime import datetime

MEM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory.json")
DAY_START, DAY_END = 9 * 60, 18 * 60
TIPS = {
    "hydration": ["Drink a glass of water now.", "Keep a bottle at your desk and refill it twice today."],
    "exercise": ["Take a 10-minute walk.", "Do 20 squats between tasks."],
    "screen": ["Look 20 feet away for 20 seconds (20-20-20 rule).", "Take a 5-minute screen break."],
}
HIGH = ("urgent", "asap", "important", "deadline", "today")
LOW = ("someday", "maybe", "whenever")


def to_min(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def fmt(mins):
    return f"{mins // 60:02d}:{mins % 60:02d}"


def parse_time(text):
    m = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", text, re.I) or re.search(r"\b(\d{1,2}):(\d{2})\b", text)
    if not m:
        return None
    h, mi = int(m.group(1)), int(m.group(2) or 0)
    if len(m.groups()) >= 3 and m.group(3):
        ap = m.group(3).lower()
        h = h % 12 + (12 if ap == "pm" else 0)
    return f"{h:02d}:{mi:02d}" if h < 24 and mi < 60 else None


def parse_task(text):
    low = text.lower()
    pr = "high" if any(w in low for w in HIGH) else "low" if any(w in low for w in LOW) else "medium"
    title = re.sub(r"^(remind me to|remember to|i need to)\s+", "", text.strip(), flags=re.I)
    t = parse_time(text)
    title = re.sub(r"\s*\b(at|by)\s+\d{1,2}(:\d{2})?\s*(am|pm)?\b", "", title, flags=re.I).strip()
    return {"title": title, "time": t, "priority": pr, "done": False}


class Assistant:
    def __init__(self, path=MEM):
        self.path = path
        self.data = {"tasks": [], "events": [], "liked": {}, "disliked": {}, "last_tip": None}
        if os.path.exists(path):
            with open(path) as f:
                self.data.update(json.load(f))

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_task(self, text):
        t = parse_task(text)
        self.data["tasks"].append(t)
        self.save()
        return t

    def list_tasks(self):
        order = {"high": 0, "medium": 1, "low": 2}
        pend = [t for t in self.data["tasks"] if not t["done"]]
        return sorted(pend, key=lambda t: (order[t["priority"]], t["time"] or "99:99"))

    def summary(self):
        pend = self.list_tasks()
        if not pend:
            return "Nothing pending. Nice!"
        lines = [f"You have {len(pend)} pending task(s):"]
        lines += [f"- [{t['priority']}] {t['title']}" + (f" @ {t['time']}" if t["time"] else "") for t in pend]
        return "\n".join(lines)

    def schedule(self, title, start, minutes):
        s, e = to_min(start), to_min(start) + int(minutes)
        clash = [ev for ev in self.data["events"] if s < ev["end"] and ev["start"] < e]
        self.data["events"].append({"title": title, "start": s, "end": e})
        self.save()
        if clash:
            return "Scheduled, but overlaps with: " + ", ".join(c["title"] for c in clash)
        return f"Scheduled {title} {fmt(s)}-{fmt(e)}."

    def free_slots(self):
        cur, out = DAY_START, []
        for ev in sorted(self.data["events"], key=lambda x: x["start"]):
            if ev["start"] > cur:
                out.append((cur, ev["start"]))
            cur = max(cur, ev["end"])
        if cur < DAY_END:
            out.append((cur, DAY_END))
        return [f"{fmt(a)}-{fmt(b)}" for a, b in out]

    def tip(self):
        weights = {c: 1 + 2 * self.data["liked"].get(c, 0) for c in TIPS if self.data["disliked"].get(c, 0) < 2}
        if not weights:
            weights = {c: 1 for c in TIPS}
        cat = random.choices(list(weights), list(weights.values()))[0]
        self.data["last_tip"] = cat
        self.save()
        return f"[{cat}] {random.choice(TIPS[cat])}"

    def feedback(self, positive):
        cat = self.data.get("last_tip")
        if not cat:
            return "Ask for a tip first."
        key = "liked" if positive else "disliked"
        self.data[key][cat] = self.data[key].get(cat, 0) + 1
        self.save()
        return f"Noted. I'll {'show more' if positive else 'show fewer'} {cat} tips."


def main():
    a = Assistant()
    print("Pace assistant. Commands: add, list, summary, schedule, free, tip, like, dislike, quit")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        cmd, _, rest = line.partition(" ")
        if cmd == "quit":
            break
        elif cmd == "add":
            print("Added:", a.add_task(rest))
        elif cmd == "list":
            print(a.summary())
        elif cmd == "summary":
            print(a.summary())
        elif cmd == "schedule":
            p = rest.rsplit(" ", 2)
            print(a.schedule(p[0], p[1], p[2]) if len(p) == 3 else "usage: schedule <title> <HH:MM> <minutes>")
        elif cmd == "free":
            print("Free:", ", ".join(a.free_slots()))
        elif cmd == "tip":
            print(a.tip())
        elif cmd in ("like", "dislike"):
            print(a.feedback(cmd == "like"))
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
