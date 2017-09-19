# **Release Notes 1.0** 

***Content*** 
> Introducing Reference Application 1.0 
> Application Contributors 
> All Modules included in the release: 

## **Introducing Reference Application 1.0** 

This being the initial release , we are glad to introduce 1.0 to the community which had a scheduled internally of October 2017. The Reference Application includes a release of the fully functional MVP and the initial version is to be versioned further with every improvement towards the subsequent future releases. 

During the release process, the developer team was really approachable for any release tips to enable a successful initial milestone from the few who had the chance to use the prototyped MVP. Additionally, the team ensured speed in getting the modules worked upon and ready for the release. 

Special appreciation go to the developer team ( Flavian, Nana, David, Scott, Vicky, Daniel) and the facilitation team (Badie and Chief Bube) for leading the technical issues required for the release to be successful. 

## **Feature highlights from Reference Application 1.0:** 
**MVP** 
>1. User login 
2. Add todo tasks 
3. List todo tasks 
4. Delete todo tasks 
5. Update todo tasks 

## **Application Contributors** 

Complete list of Management and code contributors to Reference Application 1.0 
***Release Engineering team*** 
>1. David 
2. Daniel 
3. Flavian 
4. Natalie 
5. Scott 
6. Vicky 

***Facilitation team*** 
>1. Badie 
2. Chief Bube 

## **All Modules included in the release:** 

> **App functionality module:** 
| Module | version 
| ------------- |:-------------:| 
| User login | 1.0.1-alpha.1 
| Add to do | 1.0.1-alpha.1 
| List to do | 1.0.1-alpha.1 
| Update to do | 1.0.1-alpha.1 
| Delete to do | 1.0.1-alpha.1 

> **API developer module:** 
| Module | version | Future Plan | Details| 
| ------------- |:-------------:| -----:| -----:| 
| to-do API | 1.0.1-Beta.2 | 1.0.1-alpha.2| All db data access

Endpoint | Functionality| Access
------------ | ------------- | ------------- 
POST todo/app/v1/auth/login |Logs a user in | PUBLIC
POST todo/app/v1/auth/register | Registers a user | PUBLIC
POST todo/app/v1/todo/ | Creates a new todo | PRIVATE
GET todo/app/v1/todos/ | Lists all created todo's | PRIVATE
GET todo/app/v1/todo/id | Gets a single todo | PRIVATE
PUT todo/app/v1/todo/id | Updates todo| PRIVATE

> NB: All private endpoints require a Jason Web Token (JWT), which is gotten after logging in.