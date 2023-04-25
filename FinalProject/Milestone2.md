<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Divya Rajesh Mehta (dm767)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 10:14:13 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/dm767" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234148922-fced42dc-b559-47e3-9089-0895220c997d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show valid data filled in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234148079-c14f6195-b52a-4f49-93a1-237947e7cf88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Columns: (id, name, description, category, stock, created, modified, unit_price, visibility [true, false])<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 13px;">While a request is send the first things which happens is<br>it verifies the person who is asking is a logged-in user and has<br>valid permission to view the page, if not things are displayed according to<br>it.<br>Once the request is validated a form from WTForms is used which does<br>display on the user panel (UI) so that user can know what information<br>are need to be filled in to add a product, also it has<br>validation in it which make sure user insert a proper data and doesn&#39;t<br>add incorrect data into database. Once the form is submit it&#39;s revalidated on<br>server and then a query of insert into database is hit to store<br>the data into the database.<br></span><div><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/add">https://is601-dm767-prod.herokuapp.com/product/add</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234149100-06bc4515-af9d-49fd-afd5-f8624925e367.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should have 10 sample items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234149429-a78b5864-b152-4e0d-adc5-5058bb92b358.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result should have more than 1 Sample product shown<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234149447-6448a228-a4f7-4df2-ae04-0670118a485c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result should have more than 1 Sample product shown<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234149527-62730a04-9b95-4d78-b785-bc192784c2f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ucid and date should be in the code snippet as a comment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>A separate get request was created, which work when a user click on<br>&quot;Filter Button&quot; which send the data on what data needs to be filter<br>out. Once flask recieves it the data is checked whether it contains any<br>value to be filtered out if yes that filter is apply on a<br>particular column and the query make sure to filter those data and display<br>to the user.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/view?">https://is601-dm767-prod.herokuapp.com/product/view?</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234150205-311702d2-6343-48f1-8693-2d7f14511d53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should show non-visible products too<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>A separate get request was created, which work when a user click on<br>&quot;Filter Button&quot; which send the data on what data needs to be filter<br>out.&nbsp;Once flask recieves it the data is checked whether it contains any value<br>to be filtered out if yes that filter is apply on a particular<br>column and the query make sure to filter those data and display to<br>the user. It also has a edit button to edit product details and<br>a visibilty column which determies whether the data is shown to normal users<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/viewAdmin">https://is601-dm767-prod.herokuapp.com/product/viewAdmin</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234150205-311702d2-6343-48f1-8693-2d7f14511d53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit button on Admin Product View Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151170-57f68347-12e1-4cf3-809c-3d3d4b88c677.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should be the product view page (not admin edit page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151170-57f68347-12e1-4cf3-809c-3d3d4b88c677.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should be the admin product list page (not the shop page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151400-5b812668-44a6-4142-b9e5-b555afa4dd84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151523-bfeac919-062e-4db6-a7ef-1b2f249b85ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Editing - The value of Stock, Price and Visibility has changed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p><span style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0;<br>--tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:<br>proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ;<br>--tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0 0<br>#0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000;<br>--tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate:<br>; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ;<br>--tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; font-size: 13px;">While a<br>request is send the first things which happens is it verifies the person<br>who is asking is a logged-in user and has valid permission to view<br>the page, if not things are displayed according to it.<br style="--tw-border-spacing-x: 0; --tw-border-spacing-y:<br>0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1;<br>--tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-ordinal: ; --tw-slashed-zero:<br>; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff;<br>--tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0<br>#0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ;<br>--tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow:<br>; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ;<br>--tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;">Once the request is validated a form from<br>WTForms is used which does display on the user panel (UI) so that<br>user can know what information are need to be filled in to edit<br>a product, also it has validation in it which make sure user insert<br>a proper data and doesn&#39;t add incorrect data into database. Once the form<br>is submit it&#39;s revalidated on server and then a query of update into<br>database is hit to store the data into the database which also make<br>sure only the request product editing is been taking place.<br style="--tw-border-spacing-x: 0; --tw-border-spacing-y:<br>0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1;<br>--tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-ordinal: ; --tw-slashed-zero:<br>; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff;<br>--tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0<br>#0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ;<br>--tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow:<br>; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ;<br>--tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;"></span><div><span style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y:<br>0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ;<br>--tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing:<br>; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246<br>/ 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0<br>#0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ;<br>--tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness:<br>; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ;<br>--tw-backdrop-sepia: ; font-size: 13px;"><br></span></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/edit?id=1">https://is601-dm767-prod.herokuapp.com/product/edit?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151850-9e71c0d7-e863-4dc7-9a2e-00d33ed75b95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>There is a &quot;View&quot; link in every product which leads to Product Detail<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151937-eb9d8d36-1041-467e-8b78-185dbf453523.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Detail Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>When user click on view a product_id is pass which is added in<br>query to get details of the product and display it on the page<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/product-view?id=3">https://is601-dm767-prod.herokuapp.com/product/product-view?id=3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234151850-9e71c0d7-e863-4dc7-9a2e-00d33ed75b95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>There is a &quot;Add To Cart&quot; link in every product which leads to<br>Product Detail Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234152245-cb776df2-0899-406c-b364-0d1634d344f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show they need to be logged in or it should be<br>clearly proven a non-logged in user can&#39;t add to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234152437-b7f87f35-59e6-4a17-8fec-3fd1ecd4e065.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>My cart has product_id, customer_id and quantity, whenever some click on Add to<br>Cart the current user id is taken from session and product_id is passed<br>to arguments which are then taken as input in flask and stored in<br>database using database query, if product id are different different entries which quantity<br>are created<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>My cart has product_id, customer_id and quantity, whenever some click on Add to<br>Cart the current user id is taken from session and product_id is passed<br>to arguments which are then taken as input in flask and stored in<br>database using database query, if product id are different different entries which quantity<br>are created also if an exsisting product is tried to add from a<br>specific user and then it&#39;s update the quantity by one.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234155740-76176f1e-6944-4235-927b-30887451bf5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart View - with cart toal, sub total, and clickable link of each<br>product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>Once the data of cart of individual comes a for loop is rotated<br>to calculate sub total of individual product, which is then send to frontend<br>where a forloops is rotate to display data on UI at that moment<br>it also calculate the grand total of the cart which is then visible<br>at down, if no product are there then it will display 0.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/42/commits/11fa246b3013bfb6fede918029cfc481b4f52f24">https://github.com/dm0927/IS-601-004-Course-Section/pull/42/commits/11fa246b3013bfb6fede918029cfc481b4f52f24</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/38/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/44/commits/3d5f84f625ce2dac10f5814ffae5e53f53f85529">https://github.com/dm0927/IS-601-004-Course-Section/pull/44/commits/3d5f84f625ce2dac10f5814ffae5e53f53f85529</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/view-cart">https://is601-dm767-prod.herokuapp.com/product/view-cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234155846-f1861735-ef10-4014-935f-3fd5c938bb77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Updating<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234155904-4b0d31b6-3653-4398-911d-b6a2e9ee6ae5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Updating - The quantity of Java Programming has changed from 10 to<br>100<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234155904-4b0d31b6-3653-4398-911d-b6a2e9ee6ae5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Java Programming qty is 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234156051-63a1dac5-ebf7-47a9-b6b2-43a16b09d81a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When Java Programming qty was updated to 0, it deleted the item from<br>cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234156133-ca62ce68-d289-4974-85a6-6862e031063f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Handling quantity in Lays as -1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234156201-0b8f7435-eb72-4583-987d-6db9a68a3d2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Handling quantity in Lays as -1(Lays get&#39;s deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>Whenever an update is asked for quantity in add to cart, the code<br>is designed in such a way that makes sure any input which is<br>greater than 0 the qty is updated in the database and if the<br>quantity is 0 or in negative it is treated as 0 and that<br>particular product is deleted from user cart.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dm0927/IS-601-004-Course-Section/pull/39/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3">https://github.com/dm0927/IS-601-004-Course-Section/pull/39/commits/850b33d01f247cd5cee3ba423fa879f057c2cba3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234157274-b7b160df-f579-4bf1-b495-e710075e22ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deletion of Data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234157322-f684a188-d893-4347-a85c-83967250c192.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deletion of Data (CoKe Product is Removed)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234157408-2f684add-6142-4073-825a-fb7431231fa2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Clear Cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/27128087/234157443-a1b33a30-5304-456c-b08b-ab371f3725f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Clear Cart - All Products are removed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>There are two type of deleting.<br><br>Single Delete - Where a product id is<br>taken and that individual product data is deleted from the cart<br><br>All Delete -<br>In this it deletes all the product which are available in cart of<br>an user which are deleted from the cart<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/product/view-cart">https://is601-dm767-prod.herokuapp.com/product/view-cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Nothing new was learn, as all the outcome were mainly learn during Mileston1,<br>so many things were on the same basis just need a little alteration<br>which help me to do it very easily.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-dm767-prod.herokuapp.com/">https://is601-dm767-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/dm767" target="_blank">Grading</a></td></tr></table>