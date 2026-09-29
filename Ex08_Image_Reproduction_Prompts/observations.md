# Observations

| Version | Image | Match to reference (1-5) | What differs | Change for next version |
|---|---|---:|---|---|
| v1 | `generated_images/v1.png` | 4 | Close match in mountain layers, sunset, river, forest and mist. The sky is brighter orange than the reference and the horizon placement is not exact. | Add a pale pink upper-sky band, specify the upper-third horizon and reduce orange brightness. |
| v2 | `generated_images/v2.png` | 4 | The upper sky is paler and the river route stays close. Cloud shapes, shoreline and mountain details still vary. | No further change; those fine details vary between generations. |

The scores are visual judgments by one reviewer comparing the saved images with the sample reference. There was one generation per version, no fixed seed, and the reference itself was generated for this exercise. These scores are not a reproducible benchmark.

## Conclusion
The most useful prompt elements were spatial relationships (river entering at bottom-left and leading toward the center), palette and light direction. The targeted refinement lightened the upper sky while largely preserving the composition.

Limitations: no fixed seed was available; generated details changed between samples; the image tool did not provide a quantitative similarity score.
