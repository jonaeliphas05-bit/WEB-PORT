import flet as ft

def main(page: ft.Page):
    # Professional Showcase Branding [cite: 1]
    page.title = "Jona Eliphas - Web Portfolio 2026"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Navigation Header
    page.appbar = ft.AppBar(
        title=ft.Text("Individual Web Portfolio"),
        bgcolor=ft.Colors.SURFACE_VARIANT
    )

    # Section 1: Project Timeline [cite: 7]
    timeline = ft.Column([
        ft.Text("Project Timeline", size=25, weight="bold"),
        ft.Text("Week 1: Environment setup and Flet installation."),
        ft.Divider(),
    ])

    # Section 2: Technical Blog with Mathematical Notation [cite: 16, 20]
    # Use proper LaTeX style for the Total_Cost formula [cite: 20]
    blog = ft.Column([
        ft.Text("Technical Blog", size=25, weight="bold"),
        ft.Markdown(
            "To calculate the material costs for our project, we use the formula:\n\n"
            r"### $$Total\_Cost = \\sum_{i=1}^{71} (Q \\times P) + Overheads$$"
        ),
        ft.Divider(),
    ])

    # Section 3: MATLAB Hub 
    matlab = ft.Column([
        ft.Text("MATLAB Achievement Hub", size=25, weight="bold"),
        ft.Text("Status: Courses in progress (0/8 completed)."),
        ft.Divider(),
    ])
    
    page.add(timeline, blog, matlab)

ft.app(main)