# Specification for URDF

## Do this

    * Create a urdf using xacro
    * Make it parameterized
    * Plates are made of clear acrylic
    * Robot front is in the positive X direction
    * Support posts are all vertical. They go from 10mm below the bottom plate to 10mm above the top plate.

## Desired tfs
    * base_link: located between two wheels on bottom plate
    * base_link: Main robot body (your rotation center)
    * base_footprint: Ground projection of robot center

## Relative Positions and sizes

    * base_footprint: origin of urdf
    * Bottom and top plates (acrylic): circular links with diameter: 280mm
    * Bottom plate: base footprint + (0, 0, 65mm)
    * Top plate:  base footprint + (0, 0, 125mm)
    * base_link: base_footprint + (85mm, 0mm, 65mm)
    * Support post1 (blue): base_link + (40mm, 0, 0)
    * Support post2 (blue): support_post_1 + (-180mm, 70mm, 0)
    * Support post2 (blue): support_post_1 + (-180mm, -70mm, 0)
    * Lidar (light blue): base_link + (-40mm, 0, 130mm)
    * Wheel base: 215mm
    * Wheel diameter: 62.5mm
    * Wheel track width: 24mm
    * Wheel track: base_link + (85mm, 0, -40mm)
    * Imu: base_link (grey) + (-40mm, 0, 20mm)
    * front_marker (red): base_link + (15mm, 0, 50mm)

