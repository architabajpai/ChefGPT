from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_recipe_pdf(
    recipe_name,
    recipe_content
):

    if recipe_name is None:
        recipe_name = "Recipe"

    if recipe_content is None:
        recipe_content = "No recipe available."

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            recipe_name,
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    for line in recipe_content.split("\n"):

        story.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

    doc.build(story)

    buffer.seek(0)

    return buffer