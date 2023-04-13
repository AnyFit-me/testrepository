import os
import uuid

def generate_webpage(name, offer, submission_date):
    # Read the template file
    with open('page_template.html', 'r') as file:
        template_content = file.read()

    # Substitute the placeholders with actual values using the format method
    html_content = template_content.format(name=name, offer=offer, submission_date=submission_date)

    # Generate a unique file name
    file_name = f"{uuid.uuid4().hex}.html"

    # Save the generated HTML file
    output_dir = 'generated_pages'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, file_name)
    with open(output_file, 'w') as file:
        file.write(html_content)

    base_url = "https://AnyFit-me.github.io/testrepository/"
    return f"{base_url}{file_name}"
