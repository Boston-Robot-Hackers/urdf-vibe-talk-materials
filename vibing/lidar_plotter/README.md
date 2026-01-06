# LIDAR Visualizer

Simple script to visualize ROS 2 LIDAR scan data with polar plots.

## Usage

```bash
uv run lidar_viz.py <path_to_scan_file>
```

## Example

```bash
uv run lidar_viz.py ../topic_echo_scan.txt
```

## What it does

- Reads YAML output from `ros2 topic echo /scan`
- Creates a polar plot with:
  - Forward (0 radians) pointing North
  - Angles in radians around circumference
  - Distance in meters along radius
  - Blue dots for each valid measurement

## Dependencies

Dependencies are managed inline in the script header. `uv run` will automatically install:
- matplotlib
- numpy
- pyyaml

No separate installation needed!
