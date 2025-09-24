
<h1>Netflix Dataset Cleaning – Task 1</h1>

<h2>Objective</h2>
    <p>Clean and preprocess the Netflix dataset to make it ready for analysis.</p>

<h2>Steps Performed</h2>
    <ol>
        <li>
            <strong>Loaded Dataset</strong>
            <ul>
                <li>Loaded <code>netflix_titles.csv</code> using Pandas.</li>
                <li>Explored the dataset using <code>df.info()</code> and checked missing values.</li>
            </ul>
        </li>
        <li>
            <strong>Handled Missing Values</strong>
            <ul>
                <li>Filled missing values in <code>director</code>, <code>cast</code>, <code>country</code>, <code>date_added</code>, <code>rating</code>, and <code>duration</code> with "Unknown".</li>
            </ul>
        </li>
        <li>
            <strong>Removed Duplicates</strong>
            <ul>
                <li>Checked for duplicate rows → 0 duplicates found.</li>
            </ul>
        </li>
        <li>
            <strong>Standardized Text Columns</strong>
            <ul>
                <li>Columns <code>type</code>, <code>rating</code>, <code>country</code>, <code>cast</code>, <code>director</code> were stripped of extra spaces and converted to lowercase.</li>
            </ul>
        </li>
        <li>
            <strong>Formatted Dates</strong>
            <ul>
                <li>Converted <code>date_added</code> to proper <code>datetime</code> format.</li>
            </ul>
        </li>
        <li>
            <strong>Cleaned Column Names</strong>
            <ul>
                <li>Renamed all columns to lowercase and replaced spaces with underscores (e.g., <code>Show ID</code> → <code>show_id</code>).</li>
            </ul>
        </li>
        <li>
            <strong>Converted Numeric Columns</strong>
            <ul>
                <li>Ensured <code>release_year</code> is integer type.</li>
                <li>Extracted numeric duration from the <code>duration</code> column as <code>duration_num</code>.</li>
            </ul>
        </li>
        <li>
            <strong>Saved Cleaned Dataset</strong>
            <ul>
                <li>Cleaned dataset saved as <code>cleaned_netflix_dataset.csv</code>.</li>
            </ul>
        </li>
    </ol>

<h2>Outcome</h2>
    <p>The dataset is now free of missing values, duplicates, and inconsistencies. Column names and text formats are uniform, dates are properly formatted, and numeric values are ready for analysis.</p>

<h2>Files in this Repository</h2>
    <ul class="file-list">
        <li><code>netflix_titles.csv</code> – Raw dataset.</li>
        <li><code>task1_cleaning.py</code> – Python script for cleaning the dataset.</li>
        <li><code>cleaned_netflix_dataset.csv</code> – Cleaned and preprocessed dataset.</li>
        <li><code>README.md</code> – Summary of the cleaning process.</li>
    </ul>
