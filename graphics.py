import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D

class graphics2d:
    def __init__(self, width=8, height=6, bgcolor='white'):
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_facecolor(bgcolor)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.objects = []

    def add_rectangle(self, xy, width, height, color='blue', alpha=1.0, linewidth=1, edgecolor='black'):
        rect = patches.Rectangle(xy, width, height, linewidth=linewidth, edgecolor=edgecolor, facecolor=color, alpha=alpha)
        self.objects.append(rect)

    def add_circle(self, center, radius, color='red', alpha=1.0, linewidth=1, edgecolor='black'):
        circ = patches.Circle(center, radius, linewidth=linewidth, edgecolor=edgecolor, facecolor=color, alpha=alpha)
        self.objects.append(circ)

    def add_line(self, start, end, color='black', linewidth=2, alpha=1.0):
        line = plt.Line2D((start[0], end[0]), (start[1], end[1]), color=color, linewidth=linewidth, alpha=alpha)
        self.objects.append(line)

    def add_text(self, position, text, fontsize=12, color='black', ha='center', va='center'):
        txt = {'position': position, 'text': text, 'fontsize': fontsize, 'color': color, 'ha': ha, 'va': va}
        self.objects.append(txt)

    def render(self, xlim=None, ylim=None):
        self.ax.clear()
        self.ax.set_facecolor(self.bgcolor)
        self.ax.axis('off')
        for obj in self.objects:
            if isinstance(obj, (patches.Rectangle, patches.Circle)):
                self.ax.add_patch(obj)
            elif isinstance(obj, plt.Line2D):
                self.ax.add_line(obj)
            elif isinstance(obj, dict) and 'text' in obj:
                self.ax.text(obj['position'][0], obj['position'][1], obj['text'],
                             fontsize=obj['fontsize'], color=obj['color'],
                             ha=obj['ha'], va=obj['va'])
        if xlim:
            self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)
        else:
            self.ax.autoscale_view()
        plt.show()

# class graphics3d:
#     def __init__(self):
#         self.objects = []

#     def add_sphere(self, center, radius, color='gray'):
#         self.objects.append({
#             'type': 'sphere',
#             'center': np.array(center),
#             'radius': radius,
#             'color': color
#         })

#     def add_cylinder(self, start, end, radius, color='gray'):
#         self.objects.append({
#             'type': 'cylinder',
#             'start': np.array(start),
#             'end': np.array(end),
#             'radius': radius,
#             'color': color
#         })

#     def add_arrow(self, start, end, radius=0.05, color='blue', cone_length=0.15, cone_radius=0.1):
#         # Arrow shaft
#         shaft_end = start + (np.array(end) - np.array(start)) * (1 - cone_length / np.linalg.norm(np.array(end) - np.array(start)))
#         self.add_cylinder(start, shaft_end, radius, color)
#         # Arrow head (cone)
#         self.objects.append({
#             'type': 'cone',
#             'start': shaft_end,
#             'end': np.array(end),
#             'radius': cone_radius,
#             'color': color
#         })

#     def render(self, lim=None, ax=None):
#         if ax is None:
#             fig = plt.figure(figsize=(8,8))
#             ax = fig.add_subplot(111, projection='3d')
#         if lim is not None:
#             ax.set_xlim(lim[0])
#             ax.set_ylim(lim[1])
#             ax.set_zlim(lim[2])
#         for obj in self.objects:
#             if obj['type'] == 'sphere':
#                 self._draw_sphere(ax, obj['center'], obj['radius'], obj['color'])
#             elif obj['type'] == 'cylinder':
#                 self._draw_cylinder(ax, obj['start'], obj['end'], obj['radius'], obj['color'])
#             elif obj['type'] == 'cone':
#                 self._draw_cone(ax, obj['start'], obj['end'], obj['radius'], obj['color'])
#         ax.set_box_aspect([1,1,1])
#         ax.set_axis_off()
#         fig.patch.set_alpha(0)
#         plt.show()

#     def _draw_sphere(self, ax, center, radius, color):
#         u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
#         x = center[0] + radius * np.cos(u) * np.sin(v)
#         y = center[1] + radius * np.sin(u) * np.sin(v)
#         z = center[2] + radius * np.cos(v)
#         ax.plot_surface(x, y, z, color=color, shade=True, alpha=1.0, antialiased=False)

#     def _draw_cylinder(self, ax, start, end, radius, color):
#         v = end - start
#         mag = np.linalg.norm(v)
#         if mag == 0:
#             return
#         v = v / mag
#         not_v = np.array([1, 0, 0]) if abs(v[0]) < 0.99 else np.array([0, 1, 0])
#         n1 = np.cross(v, not_v)
#         n1 /= np.linalg.norm(n1)
#         n2 = np.cross(v, n1)
#         t = np.linspace(0, mag, 20)
#         theta = np.linspace(0, 2 * np.pi, 40)
#         t, theta = np.meshgrid(t, theta)
#         X, Y, Z = [start[i] + v[i] * t + radius * np.sin(theta) * n1[i] + radius * np.cos(theta) * n2[i] for i in range(3)]
#         ax.plot_surface(X, Y, Z, color=color, alpha=1.0, shade=True, antialiased=False)

#     def _draw_cone(self, ax, start, end, radius, color):
#         v = end - start
#         mag = np.linalg.norm(v)
#         if mag == 0:
#             return
#         v = v / mag
#         not_v = np.array([1, 0, 0]) if abs(v[0]) < 0.99 else np.array([0, 1, 0])
#         n1 = np.cross(v, not_v)
#         n1 /= np.linalg.norm(n1)
#         n2 = np.cross(v, n1)
#         t = np.linspace(0, mag, 10)
#         theta = np.linspace(0, 2 * np.pi, 40)
#         t, theta = np.meshgrid(t, theta)
#         R = (1 - t / mag) * radius
#         X, Y, Z = [start[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in range(3)]
#         ax.plot_surface(X, Y, Z, color=color, alpha=1.0, shade=True, antialiased=False)

import pyvista as pv
pv.set_jupyter_backend('trame')

class graphics3d:
    def __init__(self):
        self.plotter = pv.Plotter()
        # self.plotter.set_viewup([0, 0, 1])
        self.actors = []

    def add_sphere(self, center, radius, color='white'):
        sphere = pv.Sphere(radius=radius, center=np.array(center), theta_resolution = 30, phi_resolution = 30)
        actor = self.plotter.add_mesh(sphere, color=color, smooth_shading=True)
        self.actors.append(actor)

    def add_arrow(self, start, end, radius=0.05, color='red', cone_length=0.2, cone_radius=0.1):
        start = np.array(start)
        end = np.array(end)
        direction = end - start
        length = np.linalg.norm(direction)
        if length == 0:
            return
        direction = direction / length
        shaft_length = max(length - cone_length, 0)
        # Shaft
        if shaft_length > 0:
            shaft_end = start + direction * shaft_length
            cylinder = pv.Cylinder(center=(start + shaft_end) / 2, direction=direction, radius=radius, height=shaft_length, resolution = 30)
            self.plotter.add_mesh(cylinder, color=color, smooth_shading=True)
        # Cone
        cone_center = start + direction * (length - cone_length / 2)
        cone = pv.Cone(center=cone_center, direction=direction, height=cone_length, radius=cone_radius, resolution = 30)
        self.plotter.add_mesh(cone, color=color, smooth_shading=True)

    def add_cylinder(self, start, end, radius=0.1, color='gray'):
        start = np.array(start)
        end = np.array(end)
        direction = end - start
        height = np.linalg.norm(direction)
        if height == 0:
            return
        direction = direction / height
        center = (start + end) / 2
        cylinder = pv.Cylinder(center=center, direction=direction, radius=radius, height=height, resolution = 30)
        self.plotter.add_mesh(cylinder, color=color, smooth_shading=True)

    def render(self):
        self.plotter.view_xy()
        self.plotter.show()

class molecule:
    def __init__(self, 
                 sel, 
                 atomRadius = 0.25, 
                 bondRadius=0.05, 
                 modeDisp=None, 
                 modeScale = 1.0, 
                 arrowRadius = 0.05):
        img = graphics3d()
        atColors = []
        atRad = []
        for at in sel.atoms:
            if at.element == 'C':
                atColors.append('black')
                atRad.append(1.7)
            elif at.element == 'N':
                atColors.append('blue')
                atRad.append(1.625)
            elif at.element == 'O':
                atColors.append('red')
                atRad.append(1.5)
            elif at.element == 'H':
                atColors.append('white')
                atRad.append(1.0)
            elif at.element == 'S':
                atColors.append('yellow')
                atRad.append(1.85)
        for i, at in enumerate(sel.atoms):
            img.add_sphere(at.position, atomRadius * atRad[i], color=atColors[i])
            if modeDisp is not None:
                img.add_arrow(at.position, at.position + modeScale * modeDisp[i], arrowRadius, color='orange', cone_length=arrowRadius*3, cone_radius=arrowRadius*2)
                img.add_arrow(at.position, at.position - modeScale * modeDisp[i], arrowRadius, color='yellow', cone_length=arrowRadius*3, cone_radius=arrowRadius*2)
        for b in sel.bonds:
            idx1 = b.atoms[0].index
            idx2 = b.atoms[1].index
            start = b.atoms[0].position
            end = b.atoms[1].position
            center = (start + end) / 2
            img.add_cylinder(start, center, bondRadius, color=atColors[idx1])
            img.add_cylinder(center, end, bondRadius, color=atColors[idx2])
        # limits = [[min * 5 , max * 5] for min, max in [[-1, 1], [-1, 1], [-1, 1]]]
        img.render()

class plotSpectra:
    def __init__(self,
                 frequencies,
                 intensities,
                 xlim=None,
                 ylim=None,
                 labels=None, 
                 colors='black',
                 interpolStep=5,
                 filename=None,
                 title=None,
                 vlines=None,
                 vlineColors=None):
        plt.figure(figsize=(6,4))
        interpolationAxis = np.linspace(frequencies[0],frequencies[-1], interpolStep * len(frequencies))
        if len(np.shape(intensities)) == 1:
            # single spectrum
            intpol = CubicSpline(frequencies, intensities)
            highRes = intpol(interpolationAxis)
            if labels is None:
                plt.plot(interpolationAxis, highRes, color=colors)
            else:
                plt.plot(interpolationAxis, highRes, color=colors, label=labels)
            plt.plot(frequencies, intensities, 'o', color=colors)
        elif len(np.shape(intensities)) == 2:
            # multiple spectra
            if not isinstance(colors, list):
                colors = [colors] * len(intensities)
            if labels is not None and not isinstance(labels, list):
                labels = [labels] * len(intensities)
            for i in range(len(intensities)):
                intpol = CubicSpline(frequencies, intensities[i])
                highRes = intpol(interpolationAxis)
                if labels is None:
                    plt.plot(interpolationAxis, highRes, color=colors[i])
                else:
                    plt.plot(interpolationAxis, highRes, color=colors[i], label=labels[i])
                plt.plot(frequencies, intensities[i], 'o', color=colors[i])
        else:
            raise ValueError("intensities must be 1D or 2D array")
        if xlim is not None:
            plt.xlim(xlim[0], xlim[1])
        if ylim is not None:
            plt.ylim(ylim[0], ylim[1])
        plt.xlabel("wavenumber (cm$^{-1}$)")
        plt.ylabel("VDoS (a.u.)")
        if title is not None:
            plt.title(title)
        if vlines is not None:
            if not isinstance(vlines, list):
                vlines = [vlines]
            if vlineColors is None:
                vlineColors = ['gray'] * len(vlines)
            if not isinstance(vlineColors, list):
                vlineColors = [vlineColors] * len(vlines)
            for i, vline in enumerate(vlines):
                plt.axvline(x=vline, color=vlineColors[i], linestyle='--', linewidth=2)
        if labels is not None:
            plt.legend()
        # plt.grid()
        if filename is not None:
            plt.savefig(filename, dpi=300)
        plt.show()

# the following uses OPenGL for graphics, but still looks ugly and crashes
# need to learn how to use lighting etc.

# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *

# class graphics3d:
#     def __init__(self):
#         self.objects = []
#         self.lim = [[-10, 10], [-10, 10], [-10, 10]]
#         self.window = None

#     def add_sphere(self, center, radius, color='gray'):
#         self.objects.append(('sphere', np.array(center), radius, color))

#     def add_cylinder(self, start, end, radius, color='gray'):
#         self.objects.append(('cylinder', np.array(start), np.array(end), radius, color))

#     def _color_to_rgb(self, color):
#         # Simple color mapping, extend as needed
#         colors = {
#             'gray': (0.5, 0.5, 0.5),
#             'black': (0.0, 0.0, 0.0),
#             'white': (1.0, 1.0, 1.0),
#             'red': (1.0, 0.0, 0.0),
#             'blue': (0.0, 0.0, 1.0),
#             'yellow': (1.0, 1.0, 0.0),
#             'green': (0.0, 1.0, 0.0),
#             'cyan': (0.0, 1.0, 1.0),
#             'magenta': (1.0, 0.0, 1.0),
#         }
#         if isinstance(color, str):
#             return colors.get(color, (0.5, 0.5, 0.5))
#         return color

#     def _draw_sphere(self, center, radius, color):
#         glPushMatrix()
#         glColor3f(*self._color_to_rgb(color))
#         glTranslatef(*center)
#         quad = gluNewQuadric()
#         gluSphere(quad, radius, 32, 32)
#         gluDeleteQuadric(quad)
#         glPopMatrix()

#     def _draw_cylinder(self, start, end, radius, color):
#         # Compute direction and length
#         direction = end - start
#         length = np.linalg.norm(direction)
#         if length == 0:
#             return
#         direction = direction / length
#         # Find rotation axis and angle
#         z_axis = np.array([0, 0, 1])
#         axis = np.cross(z_axis, direction)
#         angle = np.degrees(np.arccos(np.clip(np.dot(z_axis, direction), -1.0, 1.0)))
#         glPushMatrix()
#         glColor3f(*self._color_to_rgb(color))
#         glTranslatef(*start)
#         if np.linalg.norm(axis) > 1e-6:
#             glRotatef(angle, *axis)
#         quad = gluNewQuadric()
#         gluCylinder(quad, radius, radius, length, 16, 1)
#         gluDeleteQuadric(quad)
#         glPopMatrix()

#     def _display(self):
#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         glLoadIdentity()
#         # Set camera
#         center = [(lim[0] + lim[1]) / 2 for lim in self.lim]
#         size = max(lim[1] - lim[0] for lim in self.lim)
#         gluLookAt(center[0], center[1] - size, center[2] + size/2,
#                   center[0], center[1], center[2],
#                   0, 0, 1)
#         # Draw objects
#         for obj in self.objects:
#             if obj[0] == 'sphere':
#                 self._draw_sphere(obj[1], obj[2], obj[3])
#             elif obj[0] == 'cylinder':
#                 self._draw_cylinder(obj[1], obj[2], obj[3], obj[4])
#         glutSwapBuffers()

#     def _reshape(self, w, h):
#         glViewport(0, 0, w, h)
#         glMatrixMode(GL_PROJECTION)
#         glLoadIdentity()
#         size = max(lim[1] - lim[0] for lim in self.lim)
#         gluPerspective(45, w / float(h), 0.1, 100.0 * size)
#         glMatrixMode(GL_MODELVIEW)

#     def render(self, lim=None):
#         if lim is not None:
#             self.lim = lim
#         glutInit()
#         glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
#         glutInitWindowSize(600, 600)
#         self.window = glutCreateWindow(b"PyOpenGL 3D Viewer")
#         glEnable(GL_DEPTH_TEST)
#         glClearColor(1, 1, 1, 1)
#         glutDisplayFunc(self._display)
#         glutReshapeFunc(self._reshape)
#         glutMainLoop()