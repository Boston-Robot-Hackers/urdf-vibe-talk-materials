#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib>=3.8.0",
#     "numpy>=1.26.0",
#     "pyyaml>=6.0",
# ]
# ///
# lidar_viz: Visualize LIDAR scan data from ROS2 topic echo output
# Author: Pito Salas and Claude Code
# Open Source Under MIT license

import sys
import matplotlib.pyplot as plt
import numpy as np
import yaml


def parse_ranges(raw_ranges):
    ranges = []
    for r in raw_ranges:
        if isinstance(r, str):
            ranges.append(np.nan)
        else:
            ranges.append(float(r))
    return np.array(ranges)


def visualize_scan(scan_file_path):
    with open(scan_file_path, 'r') as f:
        content = f.read()

    documents = content.split('\n---\n')
    scans = []
    for doc in documents:
        try:
            scan_data = yaml.safe_load(doc)
            if scan_data and "ranges" in scan_data:
                scans.append(scan_data)
        except yaml.YAMLError:
            continue

    if not scans:
        raise ValueError("No valid scan data found in file")

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="polar")

    max_range_overall = 0
    colors = plt.cm.rainbow(np.linspace(0, 1, len(scans)))

    for idx, scan_data in enumerate(scans):
        angle_min = scan_data["angle_min"]
        angle_max = scan_data["angle_max"]
        ranges = parse_ranges(scan_data["ranges"])

        num_measurements = len(ranges)
        angles = np.linspace(angle_min, angle_max, num_measurements)

        valid_indices = np.isfinite(ranges)
        valid_angles = angles[valid_indices]
        valid_ranges = ranges[valid_indices]

        if len(valid_ranges) > 0:
            max_range_overall = max(max_range_overall, np.max(valid_ranges))

        angle_jitter = np.random.normal(0, 0.002, len(valid_angles))
        range_jitter = np.random.normal(0, 0.01, len(valid_ranges))
        jittered_angles = valid_angles + angle_jitter
        jittered_ranges = valid_ranges + range_jitter

        alpha = 0.3 if len(scans) > 1 else 0.6
        ax.scatter(jittered_angles, jittered_ranges, s=3, c=[colors[idx]], alpha=alpha)

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_xlabel("Distance (meters)", labelpad=30)
    ax.set_title(f"LIDAR Scan ({len(scans)} scans)\nFrame: {scans[0]['header']['frame_id']}",
                 pad=20, fontsize=14)
    ax.grid(True, alpha=0.3)

    if max_range_overall > 0:
        ax.set_ylim(0, max_range_overall * 1.1)

    plt.tight_layout()
    plt.show()


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run lidar_viz.py <scan_file>")
        sys.exit(1)

    visualize_scan(sys.argv[1])


if __name__ == "__main__":
    main()
