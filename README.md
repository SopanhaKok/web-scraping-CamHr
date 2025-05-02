# CamHR Job Scraper

A Python tool for scraping job listings from the CamHR website (https://www.camhr.com) using their API.

## Purpose

This tool helps job seekers save time and effort when searching for jobs on CamHR. Instead of manually clicking through dozens of pages and job postings, this script automatically collects all relevant job listings in one place. It uses direct API requests rather than browser automation, making it much faster and more efficient than older web scraping methods.

With this tool, you can quickly find job opportunities that match your skills and interests without the tedious process of manual searching. All results are saved in a CSV file that you can easily sort, filter, and review at your convenience.

## Features

- Search for jobs using custom keywords
- Filter out expired job listings automatically
- Convert ISO format dates to human-readable format
- Export results to CSV in a specified output directory
- Handle missing fields gracefully
- Colorful terminal output for better user experience

## Installation

1. Clone this repository:
   git clone https://github.com/SopanhaKok/web-scraping-CamHr
   cd web-scraping-CamHr

2. Install the required packages:
   pip install -r requirements.txt

## Usage

Run the script with Python:
python scrape-data.py

The script will:

1. Ask you to enter a keyword to search for jobs
2. Search for jobs base on your keyword
3. Filter out expired jobs
4. Save the results to a CSV file in this format {keyword}\_{date}.csv

## Code Structure

- `scrape-data.py` - Main script that handles the job search and CSV export
- `camHr/extractor.py` - Contains the `Extractor` class that handles API requests

## Sample Output

The CSV file will have the following columns:

- `title` - Job title
- `publish_date` - When the job was published
- `expiration_date` - When the job posting expires
- `address` - Job location
- `requirement` - Job requirements
- `description` - Job description
- `is_urgent` - Whether the job is marked as urgent
- `contact_name` - Contact person's name
- `contact_phone` - Contact phone number
- `contact_email` - Contact email address
- `salary` - Salary information
- `qualification` - Required qualifications
- `major` - Required major/field of study
- `age` - Age requirements (if specified)

## Notes

- Only non-expired jobs will be included in the results
- The script uses the Asia/Bangkok timezone for date comparisons
- The default output directory is in the current working directory
