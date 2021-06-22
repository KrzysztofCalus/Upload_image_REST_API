# Upload_image_REST_API

### Django REST Framework API allowing users to upload image in PNG or JPG format.

Users are created via the admin panel
Users uploading images via HTTP request
There are three account tiers with following access.
- Basic
  - link to a thumbnail 200px in height 
- Premium
  - link to a thumbnail 200px in height
  - link to a thumbnail 400px in height
  - link to a originally uploaded image  
- Enterprise
  - link to a thumbnail 200px in height
  - link to a thumbnail 400px in height
  - link to a originally uploaded image
  - ability to fetch a link that expires after a number of seconds. User can specify number between 300-30000
    
Admins can create arbitrary plans with the following things configurable:
- thumbnail sizes
- presence of the link to the originally uploaded file
- ability to generate expiring links
