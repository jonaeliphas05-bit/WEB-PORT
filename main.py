import flet as ft

def main(page: ft.Page):
    page.title = "Jona N Eliphas | MechTek Documentation Lead Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_width = 1100
    page.window_height = 850

    # --- NAVIGATION LOGIC ---
    def navigate(e):
        index = e.control.selected_index
        # Toggle visibility based on index
        timeline_view.visible = (index == 0)
        matlab_view.visible = (index == 1)
        blog_view.visible = (index == 2)
        github_view.visible = (index == 3)
        page.update()

    # --- SECTION 1: PROJECT TIMELINE ---
    timeline_view = ft.Container(
        content=ft.Column([
            ft.Text("Project Timeline", size=32, weight="bold", color=ft.colors.BLUE_900),
            ft.Text("Weekly log of individual contributions to Group 15 (MechTek)", italic=True, size=16),
            ft.Divider(height=20),
            ft.DataTable(
                border=ft.border.all(1, "grey"),
                border_radius=10,
                heading_row_color=ft.colors.SURFACE_VARIANT,
                columns=[
                    ft.DataColumn(ft.Text("Week")),
                    ft.DataColumn(ft.Text("Documentation & Dev Tasks")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("1-2")), ft.DataCell(ft.Text("Defined Project Scope and Identification (Section 1.1)"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("3-4")), ft.DataCell(ft.Text("Mapped Industrial Maintenance Problem Statement"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("5-6")), ft.DataCell(ft.Text("Documented 8 Functional Requirements for Firebase"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("7-8")), ft.DataCell(ft.Text("Finalized System Overview and Target User Personas"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("9-10")), ft.DataCell(ft.Text("Created Firebase Firestore Data Model Schema"))]),
                ],
            )
        ]),
        padding=40,
        visible=True
    )

    # --- SECTION 2: MATLAB ACHIEVEMENT HUB ---
    matlab_view = ft.Container(
        content=ft.Column([
            ft.Text("MATLAB Achievement Hub", size=32, weight="bold", color=ft.colors.ORANGE_800),
            ft.Text("Proof of completion: 5/8 MathWorks Learning Center Courses", size=16),
            ft.Divider(height=20),
            ft.GridView(
                expand=1,
                runs_count=3,
                max_extent=300,
                child_aspect_ratio=1.2,
                spacing=20,
                run_spacing=20,
                children=[
                    # Certificate slots - Replace 'assets/matlabX.png' with your actual filenames
                    ft.Card(content=ft.Container(padding=10, content=ft.Column([ft.Image(src=f"assets/matlab{i}.png", border_radius=5, error_content=ft.Text(f"Paste Cert {i} Here")), ft.Text(f"MATLAB Course {i}", weight="bold", text_align="center")], horizontal_alignment="center")))
                    for i in range(1, 6) # Displays 5 slots as requested
                ]
            )
        ]),
        padding=40,
        visible=False
    )

    # --- SECTION 3: TECHNICAL BLOG ---
    blog_view = ft.Container(
        content=ft.Column([
            ft.Text("Confidence in Concepts", size=32, weight="bold", color=ft.colors.GREEN_800),
            ft.Markdown(
                "### Understanding Industrial Maintenance Costs\n"
                "As the Documentation Lead, I defined the financial metrics for MechTek. "
                "To calculate the total maintenance overhead, we utilize the following mathematical notation:\n\n"
                r"### $$Total Cost = \sum_{i=1}^{n} (Q_i \times P_i) + Overheads$$",
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            ),
            ft.Divider(height=30),
            ft.Text("Concept Walkthrough Video", size=20, weight="bold"),
            ft.Container(
                height=300,
                bgcolor=ft.colors.BLACK,
                border_radius=15,
                content=ft.Icon(ft.icons.PLAY_CIRCLE_FILL, color="white", size=50),
                alignment=ft.alignment.center,
                # Replace with: content=ft.Video(playlist=[ft.VideoMedia("assets/my_video.mp4")])
            ),
            ft.Text("This video explains how the Firestore database calculates 'Severity Levels' in real-time.", size=14, italic=True)
        ], scroll=ft.ScrollMode.AUTO),
        padding=40,
        visible=False
    )

    # --- SECTION 4: GITHUB EVIDENCE ---
    github_view = ft.Container(
        content=ft.Column([
            ft.Text("GitHub Evidence & Individual Impact", size=32, weight="bold", color=ft.colors.BLACK),
            ft.Text("Documentation Lead | Student ID: 224063057", size=18, color=ft.colors.GREY_700),
            ft.Divider(),
            ft.Card(
                color=ft.colors.BLUE_GREY_50,
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Individual Impact Summary", weight="bold", size=20),
                        ft.Text(
                            "I bridged the gap between raw engineering problems and technical execution by "
                            "drafting the System Requirements Specification (SRS). By defining the 'Fault Lifecycle' "
                            "(Reported -> Repairing -> Fixed), I provided the Lead Developers with a logical "
                            "framework that reduced coding errors and ensured 100% auditability of industrial machine repairs."
                        ),
                    ])
                )
            ),
            ft.Text("Verified Commit History (Latest 5)", weight="bold", size=20),
            ft.Image(src="assets/github_commits.png", border_radius=10, height=200, error_content=ft.Text("Paste Github Screenshot Here")),
            ft.ListTile(leading=ft.Icon(ft.icons.CHECK_CIRCLE, color="green"), title=ft.Text("Commit 1: Drafted SRS Section 1 & 2")),
            ft.ListTile(leading=ft.Icon(ft.icons.CHECK_CIRCLE, color="green"), title=ft.Text("Commit 2: Documented Firestore Data Model schema")),
            ft.ListTile(leading=ft.Icon(ft.icons.CHECK_CIRCLE, color="green"), title=ft.Text("Commit 3: Finalized Use Case Diagrams")),
        ], scroll=ft.ScrollMode.AUTO),
        padding=40,
        visible=False
    )

    # --- MAIN PAGE LAYOUT ---
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.LIST_ALT, label="Timeline"),
            ft.NavigationDestination(icon=ft.icons.SCHOOL, label="MATLAB"),
            ft.NavigationDestination(icon=ft.icons.BOOK_ROUNDED, label="Blog"),
            ft.NavigationDestination(icon=ft.icons.REPLY_ALL_ROUNDED, label="GitHub"),
        ],
        on_change=navigate,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    page.add(
        ft.Column([
            timeline_view,
            matlab_view,
            blog_view,
            github_view
        ], expand=True)
    )

ft.app(target=main)
