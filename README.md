<div align="center">
  <h1>
    <br/>
    <br/>
    🤖 Job Finder Agent 🤖
    <br/>
    <br/>
  </h1>
  <sup>A fully automated agent that scrapes new junior developer job offers from LinkedIn and emails them to you. Built with ❤️ by <a href="https://github.com/azizsnoussi"><strong>Aziz Snoussi</strong></a>.</sup>
  <br/>
  <br/>
  <a href="https://github.com/azizsnoussi/job-finder-agent/actions/workflows/job-notifier.yml">
    <img src="https://github.com/azizsnoussi/job-finder-agent/actions/workflows/job-notifier.yml/badge.svg" alt="Build Status" />
  </a>
  <img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="Python 3.10" />
  <a href="https://github.com/azizsnoussi/job-finder-agent/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/azizsnoussi/job-finder-agent" alt="MIT License" />
  </a>
  <img src="https://img.shields.io/badge/Last%20Updated-October%202025-brightgreen" alt="Last Updated" />
  <br/>
  <br/>
</div>

## ✨ Features

-   ✅ **Fully Automated:** Runs on a schedule via GitHub Actions, no manual intervention needed.
-   ✅ **Multi-Region Search:** Pre-configured for Europe, Tunisia, Qatar, UAE, and Saudi Arabia.
-   ✅ **Real-time Email Alerts:** Get a clean, HTML-formatted list of new jobs sent directly to your inbox.
-   ✅ **Highly Customizable:** Easily change the schedule, job titles, or search regions.
-   ✅ **100% Free:** Runs entirely on the free tier of GitHub Actions.

---

## 🚀 How It Works

The agent follows a simple, powerful workflow:

1.  **⏰ Schedule:** The GitHub Actions workflow is triggered automatically by a `cron` schedule.
2.  **⚙️ Setup:** A fresh Ubuntu environment is created, installing Python and the necessary libraries.
3.  **🐍 Scrape:** The `scraper.py` script visits LinkedIn and scrapes the latest job postings.
4.  **📄 Format:** The script generates a clean `job_offers.html` file with the results.
5.  **📧 Email:** The workflow securely emails the HTML file to you using the credentials stored in GitHub Secrets.

## 🛠️ Built With

| Technology | Description |
| :--- | :--- |
| **GitHub Actions** | For automation and scheduling. |
| **Python 3.10** | The core language for the scraping logic. |
| **Requests** | For making HTTP requests to LinkedIn. |
| **Beautiful Soup** | For parsing the HTML and extracting job data. |

---

## ⚙️ Setup and Installation

Get your personal job agent running in 3 simple steps.

### 1. Generate a Google App Password

To send emails securely, you need an **App Password** from Google.

1.  Go to your Google Account: [https://myaccount.google.com/](https://myaccount.google.com/).
2.  Go to the **Security** tab and enable **2-Step Verification**.
3.  Click on **App passwords**, create one for `Mail` on `Other (Custom name)`, and name it `GitHub Job Agent`.
4.  **Copy the 16-character password.** This is your `MAIL_PASSWORD`.

### 2. Configure GitHub Secrets

Add your credentials to the repository so the agent can use them.

1.  Go to your repository's **Settings** > **Secrets and variables** > **Actions**.
2.  Click **New repository secret** for each of the following:

| Secret Name | Value | Example |
| :--- | :--- | :--- |
| `MAIL_USERNAME` | Your full Gmail address | `xxxx@gmail.com` |
| `MAIL_PASSWORD` | The 16-character App Password | `xxxx-xxxx-xxxx-xxxx` |
| `MAIL_TO` | Your destination email address | `xxxx@gmail.com` |

### 3. Activate the Agent

Commit and push your files. The agent is now live and will run automatically.

```bash
git add .
git commit -m "docs: Redesign README with professional look"
git push
```

---

## 🎨 Customization

### Changing the Schedule

Edit the `cron` entries in `.github/workflows/job-notifier.yml`. Use [crontab.guru](https://crontab.guru/) to build your custom schedule.

```yaml
# Runs at 9 AM, 1 PM, and 5 PM UTC from Monday to Saturday
schedule:
  - cron: '0 9 * * 1-6'
  - cron: '0 13 * * 1-6'
  - cron: '0 17 * * 1-6'
```

### Changing Job Searches

Modify the `SEARCH_URLS` dictionary in `scraper.py` to add, remove, or change job queries.

```python
# scraper.py
SEARCH_URLS = {
    "Europe": "https://...",
    # Add a new search for Canada (Remote)
    "Canada (Remote)": "https://www.linkedin.com/jobs/search/?keywords=junior%20developer&location=Canada&f_TPR=r86400&f_WRA=true"
}
```

## ▶️ Manual Trigger

Want to run the agent right now?
1.  Go to the **Actions** tab in your repository.
2.  Click **Daily Job Scraper**.
3.  Click the **Run workflow** button.
