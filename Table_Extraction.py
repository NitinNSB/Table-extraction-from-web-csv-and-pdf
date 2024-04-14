import pandas as pd
import camelot as cl


def extract_tables_from_web():
    url = input("Enter the URL of the webpage containing tables: ")
    result = pd.read_html(url)
    return result


def extract_tables_from_csv():
    file_path = input("Enter the path of the CSV file: ")
    result = pd.read_csv(file_path)
    return result


def rename_columns(df):
    new_column_name = input("Enter the new column name: ")
    old_column_name = input("Enter the old column name: ")
    df.rename(columns={old_column_name: new_column_name}, inplace=True)
    return df


def extract_tables_from_pdf():
    pdf_path = input("Enter the path of the PDF file: ")
    pages = input("Enter the page numbers (separated by comma) you want to extract: ")
    flavor = "stream";
    tables = cl.read_pdf(pdf_path, pages=pages, flavor=flavor)
    return tables


def export_to_csv(df):
    file_name = input(
        "Enter the file name to export to (without extension), or type 'exit' to return to the main menu: ")
    if file_name.lower() == 'exit':
        return False
    else:
        df.to_csv(f"{file_name}.csv", index=False)
        print(f"Exported {file_name}.csv successfully.")
        return True


def main():
    while True:
        print("1. Extract tables from web")
        print("2. Extract tables from CSV file")
        print("3. Rename columns")
        print("4. Extract tables from PDF")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            tables = extract_tables_from_web()
            print(tables)
            export_option = input(
                "Do you want to export the extracted tables to a CSV file? (yes/no, or type 'exit' for main menu): ")
            if export_option.lower() == 'exit':
                continue
            elif export_option.lower() == 'yes':
                for i, df in enumerate(tables):
                    if not export_to_csv(df):
                        break
                    print(f"Exported table {i + 1} to CSV.")
        elif choice == '2':
            tables = extract_tables_from_csv()
            print(tables)
            export_option = input(
                "Do you want to export the extracted table to a CSV file? (yes/no, or type 'exit' for  main menu): ")
            if export_option.lower() == 'exit':
                continue
            elif export_option.lower() == 'yes':
                export_to_csv(tables)
        elif choice == '3':
            df = extract_tables_from_csv()
            renamed_df = rename_columns(df)
            print(renamed_df)
        elif choice == '4':
            tables = extract_tables_from_pdf()
            print(tables)
            export_option = input(
                "Do you want to export the extracted tables to a CSV file? (yes/no, or type 'exit' for the main menu): ")
            if export_option.lower() == 'exit':
                continue
            elif export_option.lower() == 'yes':
                for i, df in enumerate(tables):
                    if not export_to_csv(df):
                        break
                    print(f"Exported table {i + 1} to CSV.")

        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


main()
