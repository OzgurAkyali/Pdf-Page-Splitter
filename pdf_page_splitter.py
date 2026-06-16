import fitz

input_pdf = input("Enter the PDF file name (example: book.pdf): ").strip()
output_pdf = "split_output.pdf"

try:
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()

    print("\n--- Configuration ---")
    bolme_tipi = input(
        "How should the page be split? (Left-Right: 1, Top-Bottom: 0): "
    ).strip()

    for page_index in range(len(doc)):
        page = doc[page_index]

        rect = page.bound()
        width = rect.width
        height = rect.height

        if bolme_tipi == "1":
            mid = width / 2

            left_page = new_doc.new_page(width=mid, height=height)
            left_page.set_rotation(page.rotation)
            left_page.show_pdf_page(
                fitz.Rect(0, 0, mid, height),
                doc,
                page_index,
                clip=fitz.Rect(0, 0, mid, height)
            )

            right_page = new_doc.new_page(width=mid, height=height)
            right_page.set_rotation(page.rotation)
            right_page.show_pdf_page(
                fitz.Rect(0, 0, mid, height),
                doc,
                page_index,
                clip=fitz.Rect(mid, 0, width, height)
            )

        else:
            mid = height / 2

            top_page = new_doc.new_page(width=width, height=mid)
            top_page.set_rotation(page.rotation)
            top_page.show_pdf_page(
                fitz.Rect(0, 0, width, mid),
                doc,
                page_index,
                clip=fitz.Rect(0, 0, width, mid)
            )

            bottom_page = new_doc.new_page(width=width, height=mid)
            bottom_page.set_rotation(page.rotation)
            bottom_page.show_pdf_page(
                fitz.Rect(0, 0, width, mid),
                doc,
                page_index,
                clip=fitz.Rect(0, mid, width, height)
            )

    new_doc.save(output_pdf)
    print(f"\nProcess completed successfully: {output_pdf}")

except Exception as e:
    print(f"An error occurred: {e}")
