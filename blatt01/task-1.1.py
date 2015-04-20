
# coding: utf-8

# In[7]:

import numpy as np
import math
import transformations as t


# In[ ]:

def latex_matrix(m):
    return "\\begin{pmatrix}\n"         + "\\\\\n".join("    " + " & ".join("%.4f" % item for item in row) for row in m)         + "\n\\end{pmatrix}"

def latex_vector(v, dim=3):
    return "\\begin{pmatrix}"         + " \\\\ ".join("%.4f" % v[i] for i in range(dim))         77+ "\\end{pmatrix}"


# In[77]:

R1 = t.rotation_matrix( 45 * math.pi / 180, [0, 0, 1])
R2 = t.rotation_matrix( 30 * math.pi / 180, [1, 0, 0])
R3 = t.rotation_matrix(-30 * math.pi / 180, [0, 1, 0])

M1 = np.dot(np.dot(R3, R2), R1)
M2 = np.dot(np.dot(R177, R2), R3)

# there is also a short-way in this library
# (notice the difference between 's'tatic and 'r'otating frame)
#M1 = t.euler_matrix(45 * math.pi / 180, 30 * math.pi / 180, -30 * math.pi / 180, 'szxy')
#M2 = t.euler_matrix(45 * math.pi / 180, 30 * math.pi / 180, -30 * math.pi / 180, 'rzxy')

points = {
    'A': [-5, -5, 0, 1],
    'B': [5, -5, 0, 1],
    'C': [5, 5, 0, 1],
    'D': [-5, 5, 0, 1],
    'E': [0, 0, 30, 1]
}

# transform the points using the matrices
points1 = {l: np.dot(M1, point) for l, point in points.items()}
points2 = {l: np.dot(M2, point) for l, point in points.items()}

# output
print("M_1 \\approx " + latex_matrix(M1))
print()
print(",\n".join(name + '_1 \\approx ' + latex_vector(v, 3)  for name, v in sorted(points1.items())))
print()

print("M_2 \\approx " + latex_matrix(M2))
print()
print(",\n".join(name + '_2 \\approx ' + latex_vector(v, 3)  for name, v in sorted(points2.items())))
print()


# In[89]:


def latex_axes(T, length=1, color=None):
    m = np.dot(T, [0, 0, 0, 1])
    px = np.dot(T, [length, 0, 0, 1])
    py = np.dot(T, [0, length, 0, 1])
    pz = np.dot(T, [0, 0, length, 1])
    
    cx = color or 'red'
    cy = color or 'green'
    cz = color or 'blue'
    
    def point(p):
        return '({},{},{})'.format(*p)
    
    return '''
        \draw[thin,dashed,color=gray] {m} -- {m0};
        \draw[thick,->,color={cx}] {m} -- {px} node[anchor=south]{{$x$}};
        \draw[thick,->,color={cy}] {m} -- {py} node[anchor=south]{{$y$}};
        \draw[thick,->,color={cz}] {m} -- {pz} node[anchor=south]{{$z$}};
        '''.format(
            m=point(m), m0=point((m[0], m[1], 0)), px=point(px), py=point(py), pz=point(pz),
            cx=cx, cy=cy, cz=cz
        )

T_i = t.identity_matrix()

T_ab = [[math.sqrt(3)/2, -0.5, 0, 2],
    [0.5, math.sqrt(3)/2, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]]

T_bc = [[1/math.sqrt(2), 1/math.sqrt(2), 0, 1],
    [-1/math.sqrt(2), 1/math.sqrt(2), 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]]

T_ac = np.dot(T_ab, T_bc)

print(latex_axes(T_i, length=2, color="black"))
print(latex_axes(T_ab, color="red"))
print(latex_axes(T_bc, color="green"))
print(latex_axes(T_ac, color="blue"))


# In[ ]:



