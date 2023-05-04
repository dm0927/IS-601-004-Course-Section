<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Divya Rajesh Mehta (dm767)</td></tr>
<tr><td> <em>Generated: </em> 5/4/2023 7:40:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/dm767" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236304169-bbe724fa-633e-469a-90b3-798847e265ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should be from VS Code db extensions, Should have the following columns (id,<br>user_id, created, total_price, address, payment_method, money_received, first_name, last_name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236304278-6ec7b6ba-3460-4fae-8c7b-123c096d9214.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should be from VS Code db extensions, Should have valid data in it<br>and refer to the Orders table shown previously<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236304937-61a5cb29-a1ee-4241-8004-614227c471fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the purchase form UI from Heroku<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236304726-eff30a1a-47fe-4b2d-9af1-4151d8ed95aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the items pending purchase from Heroku<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236352206-7fd867a7-7470-4b50-9ddb-9713cd01cc65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>If Cart.unit_cost differs from Products.unit_cost display a % change to the user (show<br>a demo of this)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236305072-ef0ba430-f489-4934-9344-0a1209309319.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verify paid amount vs cart amount, Verify address pieces, Verify stock/price of items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236305151-72ad8fa4-96ca-46a3-9893-00c5e8dbb8f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verify payment method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236305422-26d16131-c0f5-41fc-998d-dbda7460989c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ensure your ucid and date are included<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236305718-0e77c5a0-bb17-46ec-8ed6-719368074cf5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid &quot;Money Received&quot; message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236305924-0c7a7664-fbab-4ae5-9fdb-ebdafa2d5d19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show unavailable stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236352206-7fd867a7-7470-4b50-9ddb-9713cd01cc65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show Price difference message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <ul><li>Once the data is received a form validates all the data. </li><li>Once done<br>there are 4 different payment option, only out one is selected it continue<br>the flow or else it will throw an error saying incorrect mode of<br>payment.</li><li>Also it does calculate quantity, basically if an order is made it will<br>see whether we have that much quantity available if not it will throw<br>an error saying insufficient quantity.</li><li>Once all the above check are done, a order<br>table entry is made where all the data is store</li><li>Once orde data is<br>stored orderitems data will be stored.</li><li>Once all the things are done it will<br>bring up to confirmation page where it says your order is confirmed and<br>you will be paid.</li></ul><br><br><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/49">https://github.com/dm0927/IS-601-004-Course-Section/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/purchase">https://is601-dm767-prod.herokuapp.com/product/purchase</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236309913-9faf299c-5479-4e7d-a530-e4314569c01a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the entire order details from the Order and OrderItems table, Including the<br>cost of each line item and the total value, Show how they purchased<br>(payment method) and how much they paid,Show a Thank you message (customize it<br>per your shop theme)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>Once the order confirmation is done, I continue the coding process over there<br>were the order and order items data is already fetched, I used those<br>pre-existing data to make sure all the things are available on the page<br>and then once things are verified I created new variable where all the<br>data is passed into new variables and then return a new html template<br>where those data are passed so a confirmation page can be poped up.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/49">https://github.com/dm0927/IS-601-004-Course-Section/pull/49</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/view-cart">https://is601-dm767-prod.herokuapp.com/product/view-cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236310730-29578627-7af0-4bc6-bf1c-1fe678745586.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should have at least a few records, A list item can be clicked<br>to view the full details in the Order Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236310856-0c67b551-4b94-4d41-b341-da7f6ebdc777.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing full details of a purchase (Order Details Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>Purchase List data comes from the order table where I get the user_id<br>from the session and display the user_id data which is available in the<br>orders table to be displayed out.<br><br>View Order Details - The order_id is passed,<br>a query is fired to get data from the order. Also from the<br>same order_id we can get data from order_details and product information.<br><br>Once all the<br>above information are retrieve we send it to the same order confirmation page<br>where those data are shown and any unnecessary data is removed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/50">https://github.com/dm0927/IS-601-004-Course-Section/pull/50</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/view-orders?id=1">https://is601-dm767-prod.herokuapp.com/product/view-orders?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236313827-49b15657-0e2f-4bac-95b7-341b962880fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing purchase history from multiple users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236314091-76614daf-a7b2-4cd8-ab23-4a10de3e1f9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing full details of a purchase (Order Details Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>Purchase List data comes from the order table where I get the user_id<br>from the session and display the user_id data which is available in the<br>orders table to be displayed out.<br style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y:<br>0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ;<br>--tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing:<br>; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246<br>/ 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0<br>#0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ;<br>--tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness:<br>; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ;<br>--tw-backdrop-sepia: ;"><br style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x:<br>0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ;<br>--tw-scroll-snap-strictness: proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset:<br>; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0<br>0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0<br>#0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ;<br>--tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale:<br>; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;">View Order Details<br>- The order_id is passed, a query is fired to get data from<br>the order. Also from the same order_id we can get data from order_details<br>and product information.<br style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0;<br>--tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom:<br>; --tw-scroll-snap-strictness: proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ;<br>--tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow:<br>0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0<br>0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert:<br>; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ;<br>--tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;"><br style="--tw-border-spacing-x:<br>0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0;<br>--tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-ordinal:<br>; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px;<br>--tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow:<br>0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ;<br>--tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia:<br>; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ;<br>--tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;">Once all the above information are<br>retrieve we send it to the same order confirmation page where those data<br>are shown and any unnecessary data is removed.<br><br>It also verify whether the request<br>was made from an user or owner if the data is asked by<br>the owner then it will be showing Email Address and username from the<br>account the order was placed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/51">https://github.com/dm0927/IS-601-004-Course-Section/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/shop-view-orders?id=9">https://is601-dm767-prod.herokuapp.com/product/shop-view-orders?id=9</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/236313194-b8b31095-f764-4a9a-9611-2ba9a7ebb25a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Cart page showing the button to place an order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>No issues face while implementing milestone3.<br><br>Learning - How with the roles system part<br>we can manipulate a single page to make visible different data depending upon<br>individual needs.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/dm767" target="_blank">Grading</a></td></tr></table>