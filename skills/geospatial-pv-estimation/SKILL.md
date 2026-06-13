---
name: geospatial-pv-estimation
description: Estimating roof area and solar potential from satellite imagery using YOLO segmentation, GSD conversion, and trigonometric tilt correction.
---

# Geospatial PV Estimation

Use this skill to calculate the solar energy potential of rooftops or land areas based on 2D geospatial imagery (e.g., satellite or drone photos).

## When to Use
- Estimating annual kWh yield for rooftop PV projects.
- Calculating CO2 reduction and payback periods.
- Converting pixel-based area measurements to real-world square meters.
- Validating residential unit demand (e.g., 1,300 kWh/unit baseline).

## Core Formulas

1. **GSD (Ground Sample Distance) Conversion**:
   - `Real Area (m2) = Pixel Count * (GSD^2)`
   - *Example*: 0.05 m/pixel GSD means 1 pixel = 0.0025 m2.

2. **Trigonometric Tilt Correction**:
   - 2D imagery captures the "footprint" (projected area). To get the actual roof surface area:
   - `Actual Area = Projected Area / cos(tilt_angle)`
   - *Correction Factor for 35° tilt*: `1 / cos(35°) ≈ 1.221`.

3. **Energy Yield Estimation**:
   - `Annual Yield (kWh) = Area * Solar Irradiance * PR (Performance Ratio)`
   - *Standard PR*: ~0.75 - 0.80.

## Material Constraints
- **Viable**: Concrete tile, metal sheet (Load: 15–25 kg/m²).
- **Excluded**: Asbestos-cement, thatch (due to structural or safety risks).

## Workflow
1. **Segmentation**: Use YOLOv8s-seg or similar models to isolate roof polygons.
2. **Identify GSD**: Determine the resolution of the source image (e.g., 0.05 m/pixel).
3. **Measure Footprint**: Calculate pixel area within the segmented polygon.
4. **Apply Correction**: Multiply by the tilt factor (e.g., 1.221 for 35°).
5. **Calculate Metrics**:
   - Annual kWh.
   - CO2 Offset (e.g., 0.87 kg CO2 per kWh in certain regions).
   - Payback Period (Investment / Annual Savings).

## Example
- **Input**: 1000 pixels, 0.05 GSD, 35° tilt.
- **Projected Area**: 1000 * 0.0025 = 2.5 m2.
- **Actual Area**: 2.5 * 1.221 = 3.05 m2.
