# Preface
Hello, user! Welcome to "Panda Cloud"! In this file, you can know the following information:
(1) About the operation of the program;
(2) Procedure instructions;
(3) About developers.
If you want to use this software, please read the following instructions in detail.

Project address: [Click here to the project.](https://pandaoxi.coding.net/public/pandaoxi/PanDaoxi/git/files/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Panda_Cloud)

# Operation Requirements of the Program
This program is divided into client and server. The server needs to run on a host, **and the client can access it only after joining the LAN where the server is located**.

## On the Server
On the server-side host, you need to ensure that the following conditions can be met:
(1) The operating system must be Windows 7 or above;
(2) Join an available LAN;
(3) Sufficient storage capacity and memory are required for some hosts of the client to send and receive network requests;
(4) Use Python 3 and install the following dependent libraries.
> The quick installer depends on the package. You can follow the following steps:
> 1. Open the command prompt (use <kbd>windows</kbd> + <kbd>R</kbd>) and enter "`CMD.EXE`".
> ![](https://img-blog.csdnimg.cn/5ad508ba2968412b80c2d0e2b488cf47.png)
> 2. Enter the following command:
> ```powershell
> pip install django
> pip install colorama
> ```
> 3. After successful installation, it will be completed!

If you see this, you can open the main program of the server (which will be mentioned later).

## On the Client
On the client side, the program has low requirements for computer configuration.

> Client quick configuration tutorial:
(1) For example, open the command prompt and enter the following code:
```powershell
> pip install requests
> pip install easygui
> ```
> Without them, the program will not work properly.

If you are all right, congratulations on the completion of the client installation.

# Program Operation Display
Hey, look at this more. It will be good for your application!

## On the Server
Directly run the server-side `use.py`.
![](https://img-blog.csdnimg.cn/d6452dc01b404bf7977452966f8e00be.png)

Running test of server:

If you see an interface like this, it means that your server has started running. As shown in the figure, the IP address of the current server is the content in the red box.
![](https://img-blog.csdnimg.cn/eeffbdae1c5f46bf933c1704e56ce50d.png)

When you access the IP address of the server, the following interface appears.
![](https://img-blog.csdnimg.cn/e7faa0f1969542ad8f69ca77dcb724d8.png)
Now you can connect and use the client.

## On the Client
![](https://img-blog.csdnimg.cn/ee7e6f34953640ce9b2f3368b9e9fcaf.png)
If it is not a Windows environment, please run `client.py` (i.e. Python is required); It is recommended to use compiled `dist\client.exe` in Windows environment.

![](https://img-blog.csdnimg.cn/b1f11096cba948a486fbba676ec94e18.png)
As shown in the figure, services can be selected according to needs.

### (1) I need to upload or download files.
#### Upload Files
Click the button to pop up the selection window and select the file you need. Select the point and confirm to send.
![](https://img-blog.csdnimg.cn/f005338a58484c4bb60818ee3a2e08fa.png)

When the prompt button pops up, it means that the sending is completed and the file has been saved to the server.
![](https://img-blog.csdnimg.cn/cf84315e8d6a4a289875841385cec8f8.png)

The server also gives relevant operation information.
![](https://img-blog.csdnimg.cn/b5c6ddc2dca745f289c505836c4a2b90.png)

#### Download Files
After clicking the download file button, a selection window pops up. We can download files according to our own needs.
![](https://img-blog.csdnimg.cn/2e01802bbfc44c2495be366aa8735805.png)

The original file contents can still be obtained after selecting the location and saving.
![](https://img-blog.csdnimg.cn/9db8e96a80304586911a3e335ae96ce9.png)

![](https://img-blog.csdnimg.cn/433752a2404f47598735f76f5d53bd07.png)

Download succeeded.

![](https://img-blog.csdnimg.cn/b96b3c2a6fea45679fa0c39a3480a1aa.png)

![](https://img-blog.csdnimg.cn/90fac8c939c440e6870b68f9d2cef150.png)
There are many records sent by users on the server.

### Short URL
This function can convert any long URL into a quick link, and the program will redirect the page to the user's original page according to the demand.

![](https://img-blog.csdnimg.cn/a0a96260c02d4fb9a27df7874d156511.png)
We use `https://blog.csdn.net/PanDaoxi2020/article/details/123148637?spm=1001.2014.3001.5501` here Com means long web address.

The short URL has been created successfully. Visiting it will jump to the original page.
![](https://img-blog.csdnimg.cn/b99775a7181e47e1a1df58412d376f0f.png)

# About Authors and Procedures
The author is Pan Daoxi of Shijiazhuang City, Hebei Province. His email address is 3377063617@qq.com , please contact pandaoxi2021 on wechat.
![](https://img-blog.csdnimg.cn/e2a62d6164994d22a304267561209d28.png)

## Questions and Answers
> Q: I see that there are relevant programs on a shopping software. Is this software charging?
> A: Completely wrong. This software is 100% free. If you see information about payment, please don't trust them and send this message to the developer.


> Q: The program reports an error. What should I do?
> A: Don't panic, tell the developer the whole error window and the way to use it, and we will try our best to fix the bug.

> Q: Why does the source code look difficult to me?
> A: The source code has been confused in order not to let others take advantage of the loopholes.
> 2022.8.9: The source code of the project has been published. This article is invalid.

# Finally
Finally, I wish you a pleasant use!

# Updated Content
Panda Cloud v1.0 (2022-3-24) : **Original content, basic functions.**
Panda Cloud v1.2 (2022-4-5): **(1) Modify the bug of client file download (2) enhance the source code protection of client program (3) Modify the server user access status output (4) Merge IP modification tools and clients to make them more convenient (5) Encrypt and store the files on the server side.**

## Functions to be Realized Later
(1) Different users and groups are convenient for multiple users.
(2) Launch multiple servers for simultaneous use, and the client automatically explores the available servers in the LAN.
(3) Continue transmission at breakpoint to increase the file transmission speed.
