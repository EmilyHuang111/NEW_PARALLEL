# Line Detection and Centerline Calculation

This project is a Python-based application for detecting and displaying lines in real-time video feed using OpenCV. It includes custom line detection, centerline calculation between parallel lines, and highlights detected lines on the screen.

## Features

- **Real-Time Video Capture:** Captures video frames in real-time and processes each frame.
- **Line Detection with Hough Transform:** Detects lines using Hough Line Transform after applying Canny edge detection and Gaussian/Median blurring.
- **Centerline Calculation:** Calculates the centerline between parallel lines, displaying it on the screen if the distance between them is significant.
- **Region of Interest (ROI):** Limits detection to a rectangular region, optimizing processing and focusing on a specific area.

