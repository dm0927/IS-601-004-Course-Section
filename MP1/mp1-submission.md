<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Divya Rajesh Mehta (dm767)</td></tr>
<tr><td> <em>Generated: </em> 2/17/2023 5:43:56 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/dm767" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219611891-da41b4c1-5949-40db-97fd-4ab197ad47e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Image<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219610863-c93fa900-d19c-46ac-bbf5-cb7930ec4bd8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Missing Information<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219611096-c8981d7e-0776-42bd-8a65-76a88b434076.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Missing Information - 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219611284-1bcadee6-aaac-41a8-90d2-7bae2bcf43bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Incorrect Date &amp; Time<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219611455-3049fc7d-9aef-4aa4-a9b8-6b2a058d43d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>Firstly striping the value of name and desciption and then verifyinh whether the<br>values aren&#39;t null. Once those test case are passed, checking whether the date<br>is in proper format, if yes then storing the value in task and<br>then appending it in global variable tasks and printing a success message, if<br>the condition of validate_insert fails it will display out the proper error message<br>and stop the functioning<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219612565-56624d78-69f9-4e3d-9244-4c0063e7e4f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Process Update - 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>I am taking all the input from users and passing it to another<br>function for computing.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219613271-2d16854e-18fa-4622-853f-3670f417fc15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update Task Code 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219613373-7107447b-cc1b-421f-9c66-2f38d2b43026.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update Task Code 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219613567-2e4c94b4-276d-480a-b33f-182441009365.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index out of bound error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219614338-07593eef-17c4-4cef-b63a-287a20989813.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219614468-1473c4f4-dcdd-4bfd-a4a3-23a90d5ee376.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>If no input are change it won&#39;t update the data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>Basically, the values which are taken input are from &quot;def process_update(index)&quot; fucntion, firstly<br>removing all the unnecassary spaces from name &amp; description. Then checking whether the<br>index is available in tasks, if not then displaying a proper output message<br>for it and stoping the funciton or else it goes further and check<br>if there is any value which is empty then it would store the<br>orignal value or else it would update it with new one. After this<br>it see&#39;s whether there is any changes in new values over previous values<br>if no changes found it will print a message with a proper apporpriate<br>message or else it would be printing success message and then finally save()<br>is called.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219614846-0fc5f7d5-61c5-4edc-9f5b-3e990e2d0314.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mark Done Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219614973-3977c182-1993-4546-a97e-d32d29f15e49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure , Task Already Completed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219615099-d4f4db68-299d-4e7f-a428-c74d918f667d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success, Task Mark Completed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>The index value is check whether that index is availble in global tasks,<br>if no then it display appropriate message according to it or else it<br>goes further and store the data in local variable which then sees whether<br>the task is completed or not, if completed the print the message according<br>to it or else it udpates the lastActivivty and change &quot;done&quot; key value<br>to True, stating the task is completed and then print the success message.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219615654-ce58d800-7ad4-4c79-b802-83265c2df6ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Task Code Screen shot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219616786-02be6bd3-82ac-4874-af95-f78a43d087a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success, display the data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219616865-343d3b70-172d-45cf-90af-a00bf1c5df18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure, show&#39;s the reason of failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219617095-872dffe3-4492-4885-ab20-6f8ca73d1446.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219617520-5993d20d-bbf8-4d4a-993a-ff30742f7ca1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Code SS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219617965-cbb9a33a-55a6-45d1-b840-58121985ed0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219618120-cd1aaa2e-8830-43cb-adeb-410289c20d21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>If a user wants to delete the task they input a index value,<br>firstly we check whether the index is available in tasks If Yes, we<br>delete the task and display the appropritate message. If No, we display a<br>message<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219618262-5575a095-ee31-4e5f-b8cf-210ee9c894fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Get Incomplete Task SS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219618647-b0530ed5-946e-4fb9-8bed-fa32d8f6166a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219618846-c23fccfe-ea66-4bb1-9172-2242750a7aea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>We fetch all the tasks from global variable tasks and then loop it<br>where we check the task which are not completed by using if conidtion<br>to check whether the key &quot;done&quot; is True or False, if False we<br>store that task in local variable in list. If the list is greater<br>then 0 we list all the incompleted task or else we say &quot;No<br>Pending Task Available&quot;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219619111-612b6d19-a0d5-402d-bcd6-e67f8532660a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Over Due Task Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219619244-ae2e9f87-0d59-4660-90ba-586b5abd182f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219619421-bc358b0d-3031-4d33-9f74-eab5501a852a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>We call the global tasks and declare a variable to store all the<br>overdue tasks in it. We fetch current date &amp; time using lastActivity() function<br>and store it in a variable getCurrentTime. Then we rotate a loop taking<br>an individual task and checking whether the currentTime is greater the due time<br>and the task is not completed then we store it in the local<br>variable which we initialise before. Then we check whether the local variable _tasks<br>lenght is more then 0, if yes then we display all the over<br>due tasks or else we print a message<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219619563-5c204efe-2e0f-45cc-95ba-76da55e03ccf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Get Time Remaining Code SS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219619751-433c3185-53ce-4391-8f96-922ca5619cef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219619856-d025b3be-7bc4-4f51-bca3-569b0c003081.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>We declare the global tasks to have access to all the task which<br>are available, then we verify whether the index is available if yes we<br>continue or else we show a proper error message and stop. If we<br>continue then we convert the due date-time of the task to datetime type<br>and get current datetime using datetime.now(). Then we call two difference first find_diff_in_time()<br>two subtract two dates and return total amount of seconds from it. Then<br>we call calc_days_hrs_min_sec() to calculate days, hrs, minutes, seconds from seconds as a<br>parameter. Then we check whether the days is negative or positive and display<br>the appropriate message according to it to the user.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219620072-22f6dbb3-c47a-4185-885e-661e9b69840b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>To verify (SS - 1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219620110-0b7b0162-6c98-4c86-9593-00677a9c6022.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>To verify (SS - 2)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219620197-3128b167-d682-460a-901d-1643cdd611e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>To verify (SS - 3)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219620473-7581ab40-7bfa-4f65-8f08-e2a0b53ec129.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Initial JSON FILE<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219620713-ec507ab5-ee74-4184-a9ea-ecb733b25270.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>INSERTED NEW DATA<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/219621073-dabb58c5-73d0-40db-8107-ca71036dacf9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DELETED DATA ON INDEX 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <ol><li>There were few issues majorly with datetime conversion which I overcome through seeing<br>it online from different website.</li><li>Also came to know we can a copy a<br>whole object with .copy() function.</li></ol><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/dm767" target="_blank">Grading</a></td></tr></table>