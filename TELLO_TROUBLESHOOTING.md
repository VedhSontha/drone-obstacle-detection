# DJI Tello Flight Connection & Troubleshooting Guide

This guide describes how to configure, debug, and optimize network connections when running the hybrid autopilot systems on the **DJI Tello** quadcopter.

## 📡 Network & Socket Specifications
The DJI Tello operates as a Wi-Fi Access Point (AP) and communicates via UDP sockets.
* **Drone IP Address:** `192.168.10.1` (Static)
* **Control Port (UDP):** `8889` (For sending SDK text commands and receiving responses)
* **State Port (UDP):** `8890` (For receiving state telemetry packet streams)
* **Video Stream Port (UDP):** `11111` (For receiving H.264 encoded raw video stream packets)

## 🛠️ Connection Checklist
1. **Connect to Wi-Fi:** Power on the Tello drone, search for the network `TELLO-XXXXXX` on your host PC, and connect. No password is required by default.
2. **Disable Mobile Data / Ethernet:** If your laptop remains connected to Ethernet or has cellular fallback active, Windows/macOS might route UDP packets through the wrong adapter. Temporarily disable other active network interfaces.
3. **Verify Connection:** Ping the drone to ensure connectivity:
   ```bash
   ping 192.168.10.1
   ```

## ⚠️ Troubleshooting Common Flight Errors

### 1. "Failed to receive video stream on port 11111"
* **Cause:** The drone's video stream is disabled by default until explicitly activated via the control socket.
* **Fix:** Verify that the control script successfully sends the `streamon` command to the drone. If it fails, restart the flight script.

### 2. High Latency or Video Lag (Optical Flow Drifts)
* **Cause:** Wi-Fi channel congestion or packet drops on UDP.
* **Fix:**
  - Keep the drone within a 10-meter range for direct line-of-sight signal quality.
  - Close background downloads or apps using heavy network resources.
  - In `FlowDroNeTello.py`, reduce the frame resolution or skip processing alternate frames (e.g., run YOLO inference every 2nd frame) to lower the computational load on the CPU.
