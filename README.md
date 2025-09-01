# 🕸️ Python Web Scraping Project 🐍✨

Welcome to my **Web Scraping** project! 🚀  

This project is a small Python script that scrapes authors from a website across **all pages** 📄➡️📄.  

## What it does 🛠️

- 🔍 Navigates through all pages of the site  
- 📝 Extracts authors from a specific HTML tag (`.author`)  
- 🧹 Cleans and sorts the authors so that each one appears **only once** ✅  
- 💾 Prints the final list of unique authors  

## How it works ⚡

1. Uses `requests` to fetch each page 🌐  
2. Parses HTML with `BeautifulSoup` 🍲  
3. Selects the authors via their CSS class (`.author`) 🎯  
4. Stores authors in a **set** to ensure uniqueness 🗃️  
5. Loops until no more authors/pages are found 🔄  

## Tech Stack 🖥️

- Python 🐍  
- Requests library 📥  
- BeautifulSoup4 🍲  

## Notes 💡

- Duplicate authors are automatically removed  
- Works for multiple pages until the website stops returning new authors  
- Simple, lightweight, and effective 🏋️  

---

Feel free to ⭐ the repo if you like it!  

Happy scraping! 🕷️💛
