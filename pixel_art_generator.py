class PixelArt:
    """A simple pixel art generator that creates and renders pixel-based artwork as ASCII art."""

    def __init__(self):
        self.canvas = None
        self.width = 0
        self.height = 0

    def create_canvas(self, width, height):
        """Initialize a blank canvas with the given dimensions.

        Args:
            width: The width of the canvas in pixels.
            height: The height of the canvas in pixels.
        """
        self.width = width
        self.height = height
        self.canvas = [['.' for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        """Set a pixel at the given coordinates to a color.

        Args:
            x: The x-coordinate (column) of the pixel.
            y: The y-coordinate (row) of the pixel.
            color: A single character representing the pixel color.

        Raises:
            ValueError: If coordinates are out of bounds or canvas is not initialized.
        """
        if self.canvas is None:
            raise ValueError('Canvas not initialized. Call create_canvas() first.')
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError(f'Coordinates ({x}, {y}) out of bounds for canvas size {self.width}x{self.height}.')
        self.canvas[y][x] = color

    def render_ascii(self):
        """Render the canvas as ASCII art and return it as a string.

        Returns:
            A string representation of the canvas with each row on a new line.

        Raises:
            ValueError: If the canvas is not initialized.
        """
        if self.canvas is None:
            raise ValueError('Canvas not initialized. Call create_canvas() first.')
        return '\n'.join(' '.join(row) for row in self.canvas)
