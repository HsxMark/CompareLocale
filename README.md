

# Locale Key Comparison Tool

This script is designed to compare locale JSON files in a multilingual project to identify missing or extra keys in different language files. It provides a quick way to ensure consistency across locale files, helping maintain translation quality and completeness.

---

## Features

- **Cross-Locale Comparison**: Compares all language JSON files against a reference locale.
- **Visual Feedback**: Highlights missing keys in **red** and extra keys in **green**, similar to `git status` formatting.
- **Sorting**: Keys are sorted alphabetically for easier comparison.
- **Configurable Reference Locale**: Specify the reference locale as a command-line argument.

---

## Requirements

- Python 3.7+
- `json` and `termcolor` libraries (installable via pip if not already available).

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/locale-comparator.git
   cd locale-comparator
   ```

2. Install required Python packages:

   ```bash
   pip install termcolor
   ```

---

## Usage

1. Place your locale JSON files in a folder named `locales` in the root directory.

2. Run the script with the desired reference locale:

   ```bash
   python compare_locales.py en
   ```

3. The script will output results to the terminal, showing missing and extra keys for each language file compared to the reference.

---

## Output Example

```bash
Comparing locale: en vs zh-Hans
+ extra_key_in_zh_hans
- missing_key_in_zh_hans

Comparing locale: en vs fr
+ extra_key_in_fr
- missing_key_in_fr
```

- `+` (Green): Keys present in the target locale but not in the reference.
- `-` (Red): Keys present in the reference locale but missing in the target.

---

## Notes

- Ensure all locale JSON files are formatted properly before running the script.
- The `locales` folder is expected to have the following structure:

  ```
  locales/
  ├── en.json
  ├── zh-Hans.json
  ├── fr.json
  ```

- Use a JSON validator if errors occur.

---

## Contributing

1. Fork the repository.
2. Create your feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature description"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For issues or suggestions, please open an issue on the repository or contact me at [your-email@example.com](mailto:your-email@example.com).
