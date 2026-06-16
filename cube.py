import math, time, os, sys

def clear():
    print("\033[H", end="")

def get_terminal_size():
    try:
        cols, rows = os.get_terminal_size()
    except:
        cols, rows = 80, 24
    return cols, rows

def rotate(x, y, z, ax, ay, az):
    # Rotate around X
    y, z = y*math.cos(ax) - z*math.sin(ax), y*math.sin(ax) + z*math.cos(ax)
    # Rotate around Y
    x, z = x*math.cos(ay) + z*math.sin(ay), -x*math.sin(ay) + z*math.cos(ay)
    # Rotate around Z
    x, y = x*math.cos(az) - y*math.sin(az), x*math.sin(az) + y*math.cos(az)
    return x, y, z

def project(x, y, z, width, height, fov=3, viewer_distance=6):
    factor = fov / (viewer_distance + z)
    px = x * factor * width/4 + width/2
    py = -y * factor * height/2 + height/2
    return int(px), int(py)

def draw_cube(ax, ay, az):
    cols, rows = get_terminal_size()
    
    # Cube vertices
    vertices = [
        (-1,-1,-1), ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1),
        (-1,-1, 1), ( 1,-1, 1), ( 1, 1, 1), (-1, 1, 1),
    ]
    
    # Edges
    edges = [
        (0,1),(1,2),(2,3),(3,0),  # back face
        (4,5),(5,6),(6,7),(7,4),  # front face
        (0,4),(1,5),(2,6),(3,7),  # connecting edges
    ]
    
    # Rotate all vertices
    rotated = [rotate(x, y, z, ax, ay, az) for x, y, z in vertices]
    projected = [project(x, y, z, cols, rows) for x, y, z in rotated]
    
    # Canvas
    canvas = [[' '] * cols for _ in range(rows - 1)]
    
    # Draw edges with line drawing
    for v1, v2 in edges:
        x1, y1 = projected[v1]
        x2, y2 = projected[v2]
        
        steps = max(abs(x2-x1), abs(y2-y1), 1)
        for i in range(steps + 1):
            t = i / steps
            x = int(x1 + (x2-x1) * t)
            y = int(y1 + (y2-y1) * t)
            if 0 <= x < cols and 0 <= y < rows - 1:
                # Pick char based on angle
                dx = abs(x2-x1)
                dy = abs(y2-y1)
                if dx > dy * 2:
                    ch = '─'
                elif dy > dx * 2:
                    ch = '│'
                else:
                    ch = '·'
                canvas[y][x] = ch
    
    # Draw vertices as bright dots
    for px, py in projected:
        if 0 <= px < cols and 0 <= py < rows - 1:
            canvas[py][px] = '◆'
    
    return '\n'.join(''.join(row) for row in canvas)

def main():
    ax, ay, az = 0, 0, 0
    print("\033[2J\033[?25l", end="")  # clear screen, hide cursor
    try:
        while True:
            clear()
            frame = draw_cube(ax, ay, az)
            print(frame, end="", flush=True)
            ax += 0.03
            ay += 0.05
            az += 0.02
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\033[?25h\033[2J\033[H", end="")  # restore cursor, clear

if __name__ == "__main__":
    main()
