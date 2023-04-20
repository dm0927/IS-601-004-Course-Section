<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Divya Rajesh Mehta (dm767)</td></tr>
<tr><td> <em>Generated: </em> 4/20/2023 1:03:57 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/dm767" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233139299-808dac81-a84d-4335-8c46-d149c4d60a74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid email validation, Show passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233146304-437db6ee-65f8-4b05-8888-0575c7a7a6a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233146555-75e5c0d8-b537-49f7-9419-6d20ae5bfb52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233146961-703adf4b-9834-490e-a331-f0b745bc23d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233147103-dea57de4-684a-4168-8363-9df2fdeed77c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233147561-146949d9-58d9-4805-9521-02f5cfd8357c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 should be present in this screenshot.<br>Clearly highlight which row it is.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">Explains how the form is handled and behaves - I have<br>WTForms to create the front-end which has inbuild validation for it. The form<br>does have the prerequisite for validation of email and username and checking whether<br>the password is long and is the same as the confirmed password.</span><div><span style="font-size:<br>13px;"><br></span></div><div><span style="font-size: 13px;">Explains the validation logic (frontend and backend) - The frontend makes<br>sure no field is left blank and has all the standard rules created<br>at the backend as in the password should be 8 digits or bigger,<br>a proper email should be available from the user, also the backend to<br>make sure that stuff is proper and acts according to it.</span></div><div><span style="font-size: 13px;"><br></span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;How the password is handled - The password is handled through the<br>WTForm where a minimum characters of length is required to pass the data<br>further, once the password is pass and the checks are validated of the<br>password then the password is encrypted to make sure no can get access<br>to it.<br><br>How DB is utilized - All the information once hit to server<br>and then passing all the validation request is then store into database. So<br>in future the user who created the account can have access to it.</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233258789-49ff9728-c9f4-4613-9df8-9d613f25abbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233258825-4ada0dff-5533-4544-a214-3a684dceda4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233258899-83ffdec1-ad36-40d0-8865-53ef576c24c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should have a flash message and/or a redirect to a landing page (post-login)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">Explains how the form is handled and behaves -&nbsp;</span><span style="font-size: 13px;">&nbsp;I<br>have WTForms to create the front-end which has inbuild validation for it. The<br>form does have the prerequisite for validation of email and password. Once both<br>data is provided a server call is made.</span><div><span style="font-size: 13px;"><br></span><span style="font-size: 13px;">Explains the<br>validation logic (frontend and backend) - The frontend doesn&#39;t have a large amount<br>of validation, as it only makes sure the input given by the user<br>is proper. Once it&#39;s hit the server validates data at backend once again<br>and then search for a specific email address in the database, if found<br>it will be returning the password or else a error would be thrown<br>saying &quot;Invalid User&quot;.<br></span><span style="font-size: 13px;"><br></span><span style="font-size: 13px;">Explains how the password is handled -<br>Once the email is found from the database, we compare the password which<br>is store in the database and the once which was inputted by the<br>user if both match we redirect the user to landing page or else<br>we through an error saying the password is incorrect</span><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233259602-3d9a3949-d715-49f9-abaa-df53e871d121.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233259665-ddbf49fd-8e47-4f15-a205-9765b542ee65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">Describe the session logic and how it&#39;s used for login -<br>Once the login is successful we create a session in python using flask_login<br>library which handles the session, it makes sure the authentication of the user<br>and whether the user which is trying to gain access of the data<br>is authorized to do that.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233259665-ddbf49fd-8e47-4f15-a205-9765b542ee65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233260006-a46b1855-6859-44f1-8460-bd7cce4cf823.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about not having proper role or permission (i.e., different<br>than the not logged in message)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233260106-031aff09-fede-4b60-94ee-70fe1fefa554.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Must have at least one valid record from the lessons (i.e., Admin)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233260180-6111292d-f380-4b70-91b9-cc014de3b467.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Include a screenshot of the Users table highlighting your admin user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">Explain how the session is used and any relevant helpers -&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;Once the login is successful we create a session in python using<br>flask_login library which handles the session, it makes sure the authentication of the<br>user and whether the user which is trying to gain access of the<br>data is authorized to do that.</span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">Explain how the session is used and any relevant helpers -<br>There can be multiple user with different categories on a single website which<br>do can have different certain tasks to make sure, the authorized user after<br>been logged in can only get access to those part we used role-access<br>module which make sure no unauthorized user is coming to get the data.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233260699-a57ff57a-033a-4c84-bc2c-11d819a1384b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navigation should be styled, UI shouldn&#39;t have any odd artifacts that are unstyled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233260685-1c3e11bd-93ce-494d-862d-caeedf48426e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Forms should be styled, Data output should be in a clean manner (i.e.,<br>table, row/cols, list groups, etc) Basically not exactly like dumped plaintext<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>CSS - I haven&#39;t did a lot of CSS work, I have a<br>bootstrap to make place my CSS, there are different option available in bootstrap<br>to design a website.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233146961-703adf4b-9834-490e-a331-f0b745bc23d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233146555-75e5c0d8-b537-49f7-9419-6d20ae5bfb52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233258789-49ff9728-c9f4-4613-9df8-9d613f25abbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This can include previous screenshots of protected pages and/or validation messages.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>The first two image would have thrown errors as only unique data can<br>be present in database from email and username, due to which exception could<br>be thrown, to handle that part I just used sql queries which determines<br>whether the data is available if yes then the error is thrown.<br><br>The third<br>compare the&nbsp; password with the database if it&#39;s incorrect it will stay on<br>login page and a flash message will appear saying &quot;Invalid Password&quot;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233261486-6002a4b9-d282-44d1-91c8-52c1f5578596.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username should prefill properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The current data is retrieved from the session using current_user once done I<br>used WTForm library to pass along those data so it can be displayed<br>automatically.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233261676-db33b092-17f9-414c-bf9b-638d18eee865.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233261695-5443ac70-ad17-48ae-b96b-91cde2bde221.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233261793-6b7ad0e0-170c-429d-a0bd-9ea9e8efa76d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233262000-deb8baf1-4c01-464d-93e9-87ed6dc67306.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email/username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233262077-1b1ac3c5-d03f-4668-ba88-83f50f697036.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/233262625-0989ba70-1ad4-4efb-a89f-38765901c66a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Second Screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc">https://github.com/dm0927/IS-601-004-Course-Section/pull/31/commits/37cbf58000d9e5a99fc2042e2fe1c58d044d15cc</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p><span style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0;<br>--tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:<br>proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ;<br>--tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0 0<br>#0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000;<br>--tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate:<br>; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ;<br>--tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; font-size: 13px;">I have<br>used sessino to find out the&nbsp; current user so I can getId of<br>that user to update the informaiton. I have WTForms to create the front-end<br>which has inbuild validation for it. The form does have the prerequisite for<br>validation of email and password. Once both data is provided a server call<br>is made.&nbsp;</span><span style="font-size: 13px;">The frontend doesn&#39;t have a large amount of validation, as<br>it only makes sure the input given by the user is proper. Once<br>it&#39;s hit the server validates data at backend once again and then search<br>for a specific email address in the database, if found it will be<br>returning the password or else a error would be thrown saying &quot;Invalid User&quot;.&nbsp;</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;Once the email is found from the database, we compare the password<br>which is store in the database and the once which was inputted by<br>the user if both match we redirect the user to landing page or<br>else we through an error saying the password is incorrect</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Flask_Login - I always used direct session to handle unauthorized access to login<br>protected url, but the flask_login library handle that part which is eventually great<br>for me.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/">https://is601-dm767-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/dm767" target="_blank">Grading</a></td></tr></table>