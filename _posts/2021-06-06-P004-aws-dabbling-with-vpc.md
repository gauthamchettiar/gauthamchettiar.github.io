---
title:  "☁️ AWS | Dabbling with VPC"
layout: post
categories: [aws]
image: /assets/img/P004/cover.png
description: "This is a beginner article, that focuses on AWS's VPC. If you just got into AWS and would like to crack any AWS Certification Exam, this could be extremely useful for you."
customexcerpt: "This is a beginner article, that focuses on AWS's VPC. If you just got into AWS and would like to crack any AWS Certification Exam, this could be extremely useful for you."
---
![Cover](assets/img/P004/cover.png)
Illustration Source: "Connected World" from [https://undraw.co](https://undraw.co/){:target="_blank"}

I had decided to attempt AWS Solutions Architect Exam. So, after doing some initial learning, I went ahead and gave my first Practice Test. And... I totally bombed the VPC section! 

VPC being one of the most important part of AWS, I really had to learn it as thoroughly as I could. I read through every material I had and created my own little paper notes. This post includes those notes, just digitalized!

*To read through this, you might have to know basics of AWS - atleast an overview of all the services offered. Also, feel free to save any diagrams given here, it's for your reference!*

<br>

# Index
1. [Where is my data being stored?](#where-is-my-data-being-stored)
2. [How to make sure my resources are isolated?](#how-to-make-sure-my-resources-are-isolated)
3. [What should I take care of before deploying any resource?](#what-should-i-take-care-of-before-deploying-any-resource)
4. [How to identify my resource?](#how-to-identify-my-resource)
5. [How to reach my resource?](#how-to-reach-my-resource)
6. [What to do next?](#what-to-do-next)


<br>

## Where is my data being stored?
Amazon stores your data in blimps soaring through the sky, hence they are called Cloud Storage... 

Okay, Just Kidding! I don't expect you to fall for that. You must be at a level to understand that Cloud is nothing but data centers managed by third party (Amazon in this case). Amazon, rents out these data centers for other companies to use. This service offering is called AWS. You already knew that right... RIGHT?

AWS have actually logically clustered all it's data centers. 
1. One or Multiple **data centers** that are closely located are being called an **Availability Zone (AZ)** (N Data Centers 🔗 1 Availability Zone).
2. Two or More **Availability Zones (AZ)** that are located in same general location are being called **Regions** (N Availability Zones 🔗 1 Region)

There are several benefits of this... 

Let's say a massive cyclone hit an *AZ*, what do you think will happen? 

Well, location for each *AZ* has been choosen such that they are atleast 60 miles apart! So even if an *AZ* goes down due to some catastrophe, there is a very low chance that same would hit another *AZ*. Thus, there are multiple *AZs* to act as a backup for any failed *AZ*.

This hierarchy of *Regions, AZs and Datacenters* can be seen in the below illustration,
![](assets/img/P004/01_01.png)

---
{:style="border: 4px solid #FDC975"}

### ✍ Remember
1. Costs associated with resources differs from *Region* to *Region*, because AWS generally discounts in *Regions* where it's cheaper to operate a data center. 
2. Not all services are available in all the Regions.
3. Any resource spread across multiple AZs are considered to be Highly Available (i.e: even if an AZ goes down resource will still continue working)
4. AWS has seperate *Regions* called `GovCloud` to be used by US, only US Government organizations are allowed to use data centers in those *Regions*.
5. When you choose a region for provisioning your resources, just keep following parameters in your mind,
   - **Optimize Latency:** Make sure Users who will be primarily accessing your applications are closer to the region where you are provisioning your resource, so that latency can be minimum. 
   - **Minimize Costs:** As previously said, some services are cheaper in certain Regions. While this difference is not significant, it should be one of your deciding factor.
   - **Address Regulatory Requirements:** Some governments have regulations that does not allow it's citizen's data to be stored outside their country, such regulatory requirements must be considered as well.

---
{:style="border: 4px solid #FDC975"}

## How to make sure my resources are isolated?
It's possible to isolate your instances from others with the help of **Virtual Private Cloud (VPC)**. Consider *VPC* as a networking layer above your AWS resources, most of your AWS resources have to be assigned a *VPC*. With *VPC*, it's easier to govern how each of these resources communicate with each other and the world.

*VPC* has a boundary, **you cannot span *VPCs* accross multiple Regions** (1 VPC 🔗 1 Region). All resources provisioned within a VPC, will be created in same Region only. Since a Region may include multiple AZs, a *VPC* may include multiple AZs (1 VPC 🔗 N AZ). Also, **a Region itself can have multiple *VPCs* under it** (1 Region 🔗 N VPC).

If VPC is not enough for logical isolation of your resources, you can also create **Subnets** within any *VPC*. *Subnets* or subnetworks are just *VPCs* divided into smaller networks. 

Association between *Subnets* and AZ is similar to that of *VPC* and Regions, **you cannot span *Subnet* accross multiple AZs** (1 Subnet 🔗 1 AZ), all resources provisioned within a *subnet* will be created in same AZ. Also, **an AZ itself can have multiple *Subnets* under it** (1 AZ 🔗 N Subnets)

![](assets/img/P004/02_01.png)

---
{:style="border: 4px solid #FDC975"}

### ✍ Remember
1. When you first create an AWS account, you are provided with a default VPC along with a default Subnet.
2. You won't be charged to create or operate VPC, you will only be charged for resources that you provision within your VPC.
3. Also remember below rules,

![](assets/img/P004/02_02.png)

---
{:style="border: 4px solid #FDC975"}

## What should I take care of before deploying any resource?
Here's a beautiful diagram of AWS resources and how they interact at various levels of networking -

![](assets/img/P004/03_01.png)

If you haven't heard of all the services yet, that's okay. Just revisit this once you go through them later. But do remember, it's important to know - where your resource is getting deployed.

From above diagram,
1. **EC2 Instances** and **RDS Instances** are deployed on an *AZ*. So when you create one, you need to choose *one VPC* and *one Subnet* for both.
2. **Elastic Load Balancers** are deployed in a *Region* but confined within a *VPC*, it can route traffic to multiple AZs at once. So when you create one, you need to choose *one VPC* and *multiple Subnets*.
3. **SNS, S3, Lambda, API Gateway, DynamoDB and SQS** are all managed services by AWS, that is deployed on a *Region*. You only need to choose a *Region* and not required to choose any *VPC*.
4. **IAM and Route53** are gobal services, that can be accessed from any *Region*.

AWS offers a lot of services, but I have only included most important one's here. Before you go through any service, just try to read - how it interacts with various networking components of AWS. This can immensely help you in cracking your certifcation exam.

## How to identify my resource?
Usually any computer which is connected over a network has an IP Address assigned to it. Using this IP Address it's possible to identify and communicate with it. Similarly in AWS, every EC2 instance has an IP Address associated with it. Actually, there are 2 IP addresses, Private IP (for when communication is required to be done within VPC) and Public IP (for when instance has to be accessed over internet).

When you create your VPC you are asked to assign a CIDR block to it. Wondering what's that? Let me explain.

CIDR (Classless Inter Domain Routing) is a method to allocate IP addresses for instances. With the help of CIDR you can define a range within which IP Address of instances will be. 

So how does a CIDR look like?

![](assets/img/P004/04_01.png)

In above example, your first 16 bits are assigned for network (they act a network identifier i.e: this part of your IP address cannot be modified) and next 16 bits can be assigned to hosts (i.e: instances). 

Here are some examples to get started with,

- **`10.10.0.0/16`**  - `10.10.0.0` to `10.10.255.255` (65,536 Total IPs)

![](assets/img/P004/04_02.png)

- **`172.16.0.0/12`** - `172.16.0.0` to `172.31.255.255` (1,048,576 Total IPs)

![](assets/img/P004/04_03.png)

- **`192.168.0.0/28`** - `192.168.0.0` to `192.168.0.15` (16 Total IPs)

![](assets/img/P004/04_04.png)

Hopefully that made it clear. In case you are bad at calculations (like me 😜), you can use this nifty tool - [Subnet Calculator](https://mxtoolbox.com/subnetcalculator.aspx). This makes it easier to calculate the range of your CIDR block.

As I was previously said, when you create a VPC, you are asked to assign a CIDR block. Also, every subnet that you create will also require a CIDR block, as you might have guessed. **Subnet's CIDR block should be within it's parent VPC's CIDR block range**. 

---
{:style="border: 4px solid #FDC975"}

### ✍ Remember
1. The allowed CIDR Range in AWS is anywhere between `/16` and `/28`, which corresponds between `65,536` IPs and `16` IPs.
2. Above CIDR range is only for IPv4 address. It's also possible to set a IPv6 CIDR range, but it's not mandatory to create a VPC. In case you are new to networking, here's a nice video explaining it for you - [Internet Protocol - IPv4 vs IPv6 as Fast As Possible](https://www.youtube.com/watch?v=aor29pGhlFE).
3. Once a VPC is created with a certain CIDR range, you cannot modify it later. Only option you have is to create a new VPC as per new requirement and migrate your application from older VPC to newer one.
4. **IMPORTANT:** Whenever you create a **Subnet**, AWS reserves **first four IPs** and **last IP** for internal networking purpose. So whenever you calculate the total available IPs you might have to **reduce 5 IPs** from that count, as those are reserved. (e.g: for `10.0.0.0/24`, following IPs are reserved - `10.0.0.1`, `10.0.0.2`, `10.0.0.3`, `10.0.0.4` and `10.0.0.255`, thus out of `256 IPs` only `251 IPs` are actually available.)

---
{:style="border: 4px solid #FDC975"}


## How to reach my resource?
In networking, there are devices called `Routers`. 

Routers are like Maps 🗺️, they help machines discover other machines by providing whereabouts of each other. Routers hold a table called `Route Table`, that acts exactly like an address book. When any machine tries to communicate with another machine, it looks into *Route Table* and gets directions.

AWS tries to hide this complexity, it does not expose any of it's Routers for us to access. Instead it does allow us to create and modify *Route Tables* to handle routing within our VPC. 

Whenever a VPC is created a *Route Table* is created along with it, this is usually known as `Main Route Table`. This Table by default includes entry that allows traffic within VPC. This default entry is immutable, meaning that it cannot be modified or removed.

Whenever a Subnet is created, that Subnet is by default associated with parent VPC's *Route Table*. You can instead create a seperate *Route Table* just for a certain Subnet as well. **Subnet inherits all Routes added to VPC's *Route Table***.

So, how does a route table look like?

![](assets/img/P004/05_01.png)

If you had created a VPC with CIDR `10.10.0.0/16`, it's route table will look like the one above.

As you can see, *Route Table* only consists of 2 columns - **Destination** and **Target**. Whenever any instance tries to access any IP address from the given CIDR range, it will forward the request to local network (i.e: within your VPC).

Here's a simple diagram on how routing will happen between 2 instances inside a VPC, For below example let's consider that instance with IP `10.10.0.12` is trying to access instance with IP `10.10.1.8`.

![](assets/img/P004/05_02.png)

Given Router is invisible to us, whenever you make a request from one of your instance to another, request goes through Router that refer's the *Route Table* Created by you, or the default one in this case. Then as per route table traffic will be routed to the destination, which is `local` in this example.

*Route Table* may not look very useful now, that is because we are yet to discuss various components that would require a *Route Table* entry to work. which mostly include gateway services like - Internet Gateway (service that allows instances in VPC to access the internet),VPC Peering (service that allows instances to connect to your local infrastructure) and NAT Gateway (service that again allows instances to access internet but without assigning a Public IP to instances).


---
{:style="border: 4px solid #FDC975"}

### ✍ Remember
1. It is not possible to block access from one Subnet to another using *Route Tables*.
2. As discussed previously, You might also assign IPv6 CIDR to any VPC. Since this has to be seprately configured, it also has to be seperately present in your *Route Table* for internal routing with IPv6 address to work.
3. **Best Practice:** Keep the default *Main Route Table* with `local` only route. Each Subnet in that VPC should have it's own *Route Table* with specific routes required for any particular usecase.


---
{:style="border: 4px solid #FDC975"}



## What to do next?
Only way to remember the concepts given here is to get your hands dirty. 

AWS's interface keeps changing from time to time so it's pointless to include screenshots for creating a VPC or a Subnet, as it may get outdated in few months.

Instead, I would would suggest go through this, [VPC Getting Started](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html) - Here you will learn to Create a VPC, Launch an Instance into your VPC, Assign Elastic IP to your Instance and Access your instance. I know we haven't discussed Elastic IP yet, still there's no harm in going through the link and trying it out.

## That's it?
Yes, VPC is a lot more than what's covered in this article. We still haven't looked into networking services that enable internet connectivity like - Internet Gateway (IGW), Network Address Translation (NAT), Elastic IP Address (EIP) etc. And also services that allows you to connect VPC to your local network, allowing you to securely access any resource. Well, those are topics for another day. 

I promise to cover VPC in it's entirety any time in future!

Till then, Have a good day!