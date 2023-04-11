<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Divya Rajesh Mehta (dm767)</td></tr>
<tr><td> <em>Generated: </em> 4/10/2023 9:50:21 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/dm767" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230816371-29d0b788-b8c6-4e63-b55a-fcb2b5b91906.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-mt85 should be updated to DIAR-ucid of the student (in nav.html) &amp; URL<br>should be visible and be from heroku dev &amp; Index page&#39;s &quot;Brought to<br>you by...&quot; message should be updated to include student&#39;s firstname, ucid, and IS601<br>section<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230816473-01e7637d-7df6-4dfe-a5d7-e69a7621d417.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference should be added for company search, Relevant url_for reference should<br>be added for company add, Relevant url_for reference should be added for employee<br>search, Relevant url_for reference should be added for employee add, Relevant url_for reference<br>should be added for admin import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230816687-ce23fb33-3014-406c-9f7e-4e73feb04480.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP3_Companies table should be visible (it may be empty or populated)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230816715-4be91cb5-b083-423b-9dd6-1d55956cefb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP3_Employees table should be visible (it may be empty or populated)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230836444-1df7c3bb-49ea-431c-a0da-c9e1dfe4a8c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UCID / DB name should be visible<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230836748-4e74bb3d-1d84-4a5c-a9df-d8478362db0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should check if the file is a .csv file otherwise reject with<br>a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230836840-202a1d92-88d9-4ff8-8a92-720206d819a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>CSV file should be read from the provided stream as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230836954-fae19f77-560b-4f20-95ce-70c8fa7e8cf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracted employee data should be appended as a dict to the employee list<br>(only consider data if all fields are present for employee) &amp; Extracted company<br>data should be appended as a dict to the company list (only consider<br>data if all fields are present for company)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230837085-17afa32d-c2f6-4460-a779-60d3773083fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After each query a flash message should be generated noting how many records<br>were processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231024187-f40e882e-713c-4856-9233-d8d057e8266b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>If a particular list was empty a flash message should note that the<br>particular list wasn&#39;t loaded or was empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230837085-17afa32d-c2f6-4460-a779-60d3773083fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should show the proper success message, Should show the proper count messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230836748-4e74bb3d-1d84-4a5c-a9df-d8478362db0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230837443-2b472e27-82ab-40eb-bd4e-76303c9ae0ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the error message when the form was submitted without a file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230837604-e1688ab3-4eb8-4133-883f-ca21ea65f58d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230837773-ec8c3c91-0772-40ef-b817-9d47acac7769.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230970600-b216715e-c898-4aa0-84c6-95cb62868c1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name is required (flash proper error message if missing), last_name is required (flash<br>proper error message if missing), company doesn&#39;t require a flash and may be<br>empty/None, email is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230970895-d3589f0d-485b-4b83-b09e-dc1c974e2814.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email format should be verified (no specific rule, just as long as there&#39;s<br>some attempt that&#39;ll mostly work)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231024459-49be4b02-75af-4d31-a37a-b9b98a8d5c01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible along with the data being passed in,<br>Except block should have a user-friendly message flashed and a print() of the<br>exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230971328-f4ff73df-b5fd-4475-a9d0-994a77590f9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230971386-e53a392c-8364-488f-b3c5-5073ba38cc17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230970600-b216715e-c898-4aa0-84c6-95cb62868c1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show first_name error message, Show last_name error message, Show email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230971690-52cb06f4-c73a-4352-80da-8c5239ab302b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid employee data shown previously, Caption should refer to which<br>employee to check<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231024553-cdd5a1b0-54e6-418d-a6a2-d33769cd092d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for fn, ln, email, company, column, order, limit (exact naming<br>is required), SELECT query should be filled in properly to pull employ id,<br>first_name, last_name, email, company_id, company_name via a LEFT JOIN, append like filter for<br>first_name if provided; should have proper wildcards, append like filter for last_name if<br>provided; should have proper wildcards, append like filter for email if provided; should<br>have proper wildcards, append equality filter for company_id if provided,<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231027366-64a4933a-f6af-47de-8943-7134f0c3f0d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allowed columns<br>and order options (asc, desc) allowed_columns = [&quot;first_name&quot;, &quot;last_name&quot;, &quot;email&quot;, &quot;company_name&quot;], append limit<br>(default 10) or limit greater than or equal to 1 and less than<br>or equal to 100, provide a proper error message if limit isn&#39;t a<br>number or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231027458-04ffa7cd-a4e6-4ab3-bac2-ef8b68dbe5ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230972863-a80664b8-3170-4f1c-b816-1066a69690d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with first_name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230972947-46cdf948-fc5f-4a49-8554-5fcfbab48f6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with last_name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230973084-5f4ff7f8-eb00-4d8b-8a87-5c953b49303c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with email filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230973239-04971e6b-9b8c-469f-b82f-b8b769ce8bcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with company filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230973366-37a553a9-401d-43d3-87fa-dc59df18efb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230973449-a08fdd7c-35f9-4230-8ba1-afae38e6dbdf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231027682-c920fc3b-d45f-4352-ae38-491120054d49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form. Missing id should be handled with a flash message and redirected back<br>to employee search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231027821-cd3159aa-e400-472f-98b0-0ea0afb3be21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name is required (flash proper error message), last_name is required (flash proper error<br>message), email is required (flash proper error message), company doesn&#39;t require a flash<br>and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231027939-71fcf252-3741-4655-9544-a3326df0373a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper UPDATE query should be visible, Except blocks (two) should have a user<br>friendly message flashed and a print() of the exception, Proper SELECT query should<br>be visible, Employee data should be passed to the render_template(), <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231028103-7469e2e0-6fef-4c06-9ba4-8fca70d881a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231028139-1569bc0d-be84-4e25-8bf9-1dc1402dda49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit (should be different)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231028254-f8c12915-de53-41e4-b448-63ef60bac8ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Captions should highlight what data changed and for which record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231028325-55e41427-02c5-4c12-be8b-0473d2cb3b88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Captions should highlight what data changed and for which record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231029732-8b4d6620-35b8-4cdd-afb4-800d1c862700.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code should retrieve form data for name, address, city, state, country, zip, website,<br> name is required (flash proper error message if missing), address is required<br>(flash proper error message proper message if missing), city is required (flash proper<br>error message if missing) (doesn&#39;t require special validation), state is required (flash proper<br>error message if missing), state should be validated against pycountry package (hint see<br>geography.py and pycountry documentation),  country is required (flash proper error message if<br>missing), , country should be validated against pycountry package (hint see geography.py and<br>pycountry documentation) ,website is not required, zipcode is required (flash proper error message<br>if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231029314-d495e79f-de51-4439-be15-294fb8ae27b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible along with the data being inserted, Except<br>block should have a user-friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231029732-8b4d6620-35b8-4cdd-afb4-800d1c862700.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show name error message, Show address error message, Show city error message, Show<br>state error message, Show country error message, show zip error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231029925-1ec86939-fbf3-45a3-9ae9-969f16209849.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231029902-05af0670-d7d5-488a-96a5-2468b64c2b7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030077-954d5bf6-7da0-419f-8aa9-20bd91590c4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid company data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030298-e238a029-e145-4575-a380-2ac1a18b4d12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count (as employee) for the company (likely a sub-query is needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030363-12e0b9d6-4e25-418d-bc3d-03a38c259952.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for name, country, state, column, order, limit, append a LIKE<br>filter for name if provided; should have proper wildcards, append an equality filter<br>for country if provided, append an equality filter for state if provided, append<br>sorting if column and order are provided and within the allows columsn and<br>allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;], append limit (default 10)<br>or limit greater than or equal to 1 and less than or equal<br>to 100, provide a proper error message if limit isn&#39;t a number or<br>if it&#39;s out of bounds, Except block should have a user friendly message<br>flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030733-27259d44-c5ec-46b7-bbc2-2af3dbbd8513.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030679-9d911e3c-9a74-47db-bf46-44f43331988c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with country filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030660-0174d2c2-1505-41c7-926c-d53d1147f083.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030863-f792777b-f5b4-4c4e-91a7-2d2c3edd81a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231030914-39293bfa-2266-4d4b-9478-e28a40f96d2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231032524-3711c718-6329-4f47-8bd6-94ca9cd3b8d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form. If id isn&#39;t present flash related error message and redirect<br>to company search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231033035-a928b645-9b6c-476e-904a-d6a7e06d2fe4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name is required (flash proper error message if missing), address is required (flash<br>proper error message if missing), city is required (flash proper error message if<br>missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231033631-33ebb867-37eb-40f7-acc4-d1e6cf88381c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state is required (flash proper error message if missing), state should be validated<br>against pycountry package (hint see geography.py and pycountry documentation), country is required (flash<br>proper error message if missing), country should be validated against pycountry package (hint<br>see geography.py and pycountry documentation)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231033759-53672d86-de31-4262-a05e-70f722d78ca8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper UPDATE query should be visible with the passed in daa, Except blocks<br>(two) should have a user friendly message flashed and a print() of the<br>exception, Proper SELECT query should be visible with the passed in data, Company<br>data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231034086-aa9e6674-441a-483a-8bdc-2bfce42c3be3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231034134-7dd05ade-1114-43dc-975d-394477c61800.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit (should be different), Page should show company data<br>in both scenarios<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231034479-174928b9-ff9a-4f4c-a8b4-523b31a6b798.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Captions should highlight what data changed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231034647-8740c0f4-aac5-4966-b9c1-98f7a84f5297.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Captions should highlight what data changed<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231031149-c2457443-5223-4e12-b148-2cf58834a9ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to employee search, All request args (minus id) are passed to the<br>redirect route, Success message should be flashed if the process worked, Delete employee<br>by id, if missing should flash the related message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231031461-bcf7bf05-2257-4ab2-8330-810fba89f059.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clearly label before and after<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231031552-8718e441-44b7-4ea2-9684-a2bad08e3192.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message should be flashed if the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231032333-4a52b892-ac16-47e4-b3d4-f28393b09e3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All request args (minus id) are passed to the redirect route, Delete company<br>by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/231032368-4293860e-8f6b-4d98-a334-b3e1ec1fea6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to company search, Success message should be flashed if the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230840598-63365456-6444-4c92-bf97-8cdf51672ce1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230840675-17ba6c28-4c49-489f-a7d8-c3830085ecf8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting a company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/230838547-c8b0b25f-c4b0-430b-8a49-8af0f408ff52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case should be visible and clearly show pass/fail (results should be from<br>running pytest with -rA), Clearly label screenshots<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I just found two issues while I was completing the project.<br><br>1 - The<br>test case was getting failed, have to debug the option which helps me<br>identity that I was using the wrong name in the HTML file which<br>the test case was getting failed.<div>2 - Had little use in deployment of<br>the github workflow</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/dm767" target="_blank">Grading</a></td></tr></table>