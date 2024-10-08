# Contributing to This Repository

This guide explains how to make a Pull Request (PR) for those who are new to GitHub.

### Installing Latex
Link: https://www.latex-project.org/get/

## Step-by-Step Guide to Making a Pull Request

### Step 1: Fork the Repository
1. Navigate to the repository you want to contribute to.
2. Click on the **Fork** button at the top-right corner to create a copy of the repository under your own GitHub account.

### Step 2: Clone the Forked Repository
1. Go to your forked repository.
2. Click on the **Code** button, copy the repository URL (HTTPS, SSH, or GitHub CLI).
3. Open a terminal (or Git Bash on Windows) and run the following command to clone the repository to your local machine:

   ```bash
   git clone <your-forked-repository-url>
   ```
   
   Example:
   ```bash
   git clone https://github.com/your-username/forked-repository.git
   ```
   
4. Navigate into the cloned repository
   
   ```bash
   cd forked-repository
   ```
   
### Step 3: Create a New Branch
1.	Before making any changes, create a new branch to work on by running:

   ```bash
   git checkout -b my-new-feature
   ```

3.	Replace my-new-feature with a descriptive name for your branch.

### Step 4: Make Your Changes
1.	Edit the files in the repository using your preferred code editor.
2.	Save the files after making the necessary changes.

## Step 5: Add and Commit Your Changes

   ``` bash
   # Fork the repo and clone it locally
   git clone <your-forked-repository-url>
   
   # Navigate into the repo directory
   cd forked-repository
   
   # Create a new branch
   git checkout -b my-new-feature
   
   # Add and commit changes
   git add .
   git commit -m "Description of changes"
   
   # Push changes to GitHub
   git push origin my-new-feature
   ```

TODO
tambahkan contoh table
