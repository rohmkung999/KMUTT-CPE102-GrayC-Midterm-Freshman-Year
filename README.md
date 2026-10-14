# 💎 Gray C: Autonomous Gem-Sorting Mobile Robot
### CPE 102: Engineering Exploration — Midterm Project
**Department of Computer Engineering (CPE) | King Mongkut's University of Technology Thonburi (KMUTT)**

[![University: KMUTT](https://img.shields.io/badge/University-KMUTT-orange.svg)](https://www.kmutt.ac.th/)
[![Department: CPE](https://img.shields.io/badge/Department-CPE%20KMUTT-red.svg)](https://www.cpe.kmutt.ac.th/)
[![Course: CPE102](https://img.shields.io/badge/Course-CPE102%20Eng%20Exploration-blue.svg)]()
[![Platform: ESP32](https://img.shields.io/badge/Platform-ESP32-blue.svg)](https://www.espressif.com/)
[![Computer Vision: OpenCV](https://img.shields.io/badge/Vision-OpenCV%20%7C%20AprilTag-green.svg)](https://opencv.org/)

---

## 📌 Project Overview
Engineered by **Group Gray C** for the freshman **CPE 102 (Engineering Exploration)** midterm challenge at KMUTT. 

The robot autonomously intakes mixed gemstone tokens, singulates them to prevent jamming, detects their color via a TCS3200 sensor, and traverses an arena using overhead AprilTag/ArUco camera tracking to deposit stones into matching color zones.

---

## 👥 Team Members (Gray C - KMUTT CPE)

| Student Name | Nickname | Student ID | Primary Role |
| :--- | :--- | :--- | :--- |
| **May Thu Thu Khaing** | Huffle | `69070503402` | Software Vision Pipeline & Calibration |
| **Nyan Lin Htet** | Nyan (เนียน) | `69070503403` | Core Software & ESP32 Integration |
| **Kritapath Tanapholpaiboon** | Tan (แทน) | `69070503407` | Hardware CAD Design & Laser Fabrication |
| **Kulchayarat Anuprasert** | Naming (น้ำอิงค์) | `69070503410` | Mechanical Prototyping & Chassis Structure |
| **Natthaphat Witthayaphiroonthong** | Prompt (พร้อมท์) | `69070503419` | Hardware Architecture & Electronics |
| **Thanawat Kongchaiyantr** | Rohm (โอห์ม) | `69070503421` | CAD Modeling & Chassis Dynamics |
| **Romteela Chitvuttichot** | Ying (หญิง) | `69070503440` | Materials Fabrication & Rapid Prototyping |

---

## ⚙️ System Architecture

1. **Intake System:** Continuous rubber-band roller powered by an independent 12V DC motor and 3S LiPo battery.
2. **Internal Chute:** 30x60 cm acrylic gravity slide feeding stones sequentially to the sorter.
3. **Singulation Gate:** Aluminum can housing with a flexible plastic membrane + SG90 micro-servo gate to eject strictly 1 stone at a time.
4. **Color Recognition:** GY-31 (TCS3200) RGB sensor classifying gem colors.
5. **Overhead Tracking:** AprilTag / ArUco marker tracked by overhead webcam for real-time trajectory corrections.

---

## 🚀 Quickstart

### 1. Python Environment Setup
```bash
git clone https://github.com/your-username/gray-c-sorting-robot.git
cd gray-c-sorting-robot
pip install -r requirements.txt
python software/virtual_mapping.py
