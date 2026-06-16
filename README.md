# 🧊 Spinning Cube

A pure terminal-based 3D spinning cube animation written in Python. It projects 3D coordinates onto a 2D text canvas using rotation matrices and renders the output directly inside your terminal window using standard characters.

---

## 🚀 How to Run the Project

Follow these steps to run the application on your local machine.

### 1. Prerequisites
This project runs entirely on standard Python libraries. No external dependencies or pip packages are required. You only need Python 3 installed.

### 2. Clone the Repository
Open your terminal and run the following commands to download the project:
```
git clone [https://github.com/sahadebojyoti09-lang/Spinning_Cube.git](https://github.com/sahadebojyoti09-lang/Spinning_Cube.git)
cd Spinning_Cube
```
###3. Execute the Script
Launch the animation by executing the Python file:
```
python3 cube.py
```
(Press Ctrl + C at any time to exit the animation).

🛠️ How It Works
Mathematical Rotation: The script defines the 8 mathematical vertices of a 3D cube. It applies trigonometric rotation formulas across the X, Y, and Z axes dynamically over time.

Perspective Projection: 3D coordinates are mapped onto a 2D perspective plane using a standard field-of-view (FOV) calculation, tracking distance from a virtual camera viewport.

Dynamic ASCII Grid: The terminal size is auto-detected dynamically to scale the rendering matrix. Edges are drawn using dynamic character selections (─, │, ·) relative to line angles, and vertices are rendered as bright nodes (◆).
