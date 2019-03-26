import ezdxf
import random  # needed for random placing points


def get_random_point():
    """Creates random x, y coordinates."""
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    return x, y


# Create a new drawing in the DXF format of AutoCAD 2010
dwg = ezdxf.new('ac1024')

# Create a block with the name 'FLAG'
flag = dwg.blocks.new(name='FLAG')

# Add DXF entities to the block 'FLAG'.
# The default base point (= insertion point) of the block is (0, 0).
flag.add_polyline2d([(0, 0), (0, 5), (4, 3), (0, 3)])  # the flag as 2D polyline
flag.add_circle((0, 0), .4, dxfattribs={'color': 2})  # mark the base point with a circle
flag.add_linear_dim((1, 3), (0, 3), (4, 3), dxfattribs={'color': 2})

# Get the modelspace of the drawing.
modelspace = dwg.modelspace()

# Get 50 random placing points.
placing_points = [get_random_point() for _ in range(50)]

for point in placing_points:
    # Every flag has a different scaling and a rotation of -15 deg.
    random_scale = 0.5 + random.random() * 2.0
    # Add a block reference to the block named 'FLAG' at the coordinates 'point'.
    modelspace.add_blockref('FLAG', point, dxfattribs={
        'xscale': random_scale,
        'yscale': random_scale,
        'rotation': -15
    })

# Save the drawing.
dwg.saveas("/home/ebi/blockref_tutorial.dxf")
