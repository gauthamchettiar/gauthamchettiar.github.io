---
title: "📟 Publishing a blog using Hugo"
date: "2025-08-25T00:00:00+00:00"
description: ""
tags: ["blogging"]
draft: false
---

A no-nonsense opinionated guide to get your blog published using [hugo](https://gohugo.io/), [github](https://github.com/), [cloudflare pages](https://pages.cloudflare.com/) and [godaddy](https://www.godaddy.com/).

This publishing workflow is not meant for total beginners, but should be more of a hand-holding guide for someone:   
- who knows how to work with Git and have a github/gitlab account.
- who are comfortable working with terminal commands rather than a GUI. 
- who is comfortable writing blogs in markdown, i.e: if you know how Hugo works and you are okay with it. 
- who can navigate around web to figure out stuff, especially if something goes wrong you should be able to google and fix it. 

If you would rather prefer a more straightforward & less involved way to blog, consider an equally awesome [bear blog](https://bearblog.dev/) instead.

**Index** : 
- [Step 1 : Setting up Hugo](#step-1--setting-up-hugo)
- [Step 2 : Writing your first post](#step-2--writing-your-first-post)
- [Step 3 : Pushing to Github](#step-3--pushing-to-github)
- [Step 4 : Publishing using Cloudflare Pages](#step-4--publishing-using-cloudflare-pages)
- [Step 5 (Optional) : Setting up custom domain](#step-5-optional--setting-up-custom-domain)

## Step 1 : Setting up Hugo
1. Install Hugo : [Mac](https://gohugo.io/installation/macos) | [Windows](https://gohugo.io/installation/windows/) | [Linux](https://gohugo.io/installation/linux) 
2. Install Git : [Mac](https://git-scm.com/downloads/mac) | [Windows](https://git-scm.com/downloads/win) | [Linux](https://git-scm.com/downloads/linux) 
3. Choose a project folder, usually documents folder works :
    ```bash {lineNos=false}
    # Mac / Linux 
    mkdir ~/Documents/Projects/; cd ~/Documents/Projects/
    # Windows 
    mkdir %USERPROFILE%\Documents\Projects & cd %USERPROFILE%\Documents\Projects
    ```
4. Choose a project name (*for a personal blog something like `<your-name>-blog` just works*) and run :
   ```bash
   hugo new site <your-name>-blog
   ```
5. A new directory would be created, step into that : 
    ```bash {lineNos=false}
    # Mac / Linux 
    cd ~/Documents/Projects/<your-name>-blog
    # Windows 
    cd %USERPROFILE%\Documents\Projects<your-name>-blog
    ```
6. Initialize git repository : 
   ```bash
   git init
   ```

**Theming**
1. Choose a theme from - [themes.gohugo.io](https://themes.gohugo.io/) (e.g: [hugo-bearblog](https://themes.gohugo.io/themes/hugo-bearblog/))
2. Go to git repository of that theme using download button - 
    ![hugo download button](/code/20251106_publishing_using_hugo/hugo_download_button.png)
3. Now there are 2 ways to use this in your blog [[?](https://stackoverflow.com/questions/61505790/hugo-theme-submodule-marked-as-dirty-doesnt-update/61509786#61509786)] -  
   1. Simple but sometimes restrictive -  directly add above git project as a submodule :  
      ```bash
      git submodule add https://github.com/janraasch/hugo-bearblog.git
      ```  
   2. **(recommended)** Slight maintainance overhead but highly customizable -
      - Fork the project :  
        ![git fork button](/code/20251106_publishing_using_hugo/git_fork_button.png)
      - Add forked project as a submodule  
        ```bash
        git submodule add https://github.com/gauthamchettiar/hugo-bearblog.git
        ```
4. Add above theme to hugo.toml -  
    ```bash
    echo "theme = 'hugo-bearblog'" >> hugo.toml
    ```

## Step 2 : Writing your first post
1. Run below command to create a new post *(⚠️ this is dependent on theme implementation, check theme specific [README](https://github.com/janraasch/hugo-bearblog/blob/master/README.md) first)* -   
    ```bash
    hugo new blog/<post-subject>.md
    ```
2. A new markdown file would be created at - `content/code/<post-subject>.md`
    ![hugo md file](/code/20251106_publishing_using_hugo/hugo_md_file.png)
    Again, your file might look slightly different based on theme you choose.
3. Edit this markdown file to include your post content. 
4. Preview your blog locally :   
    ```bash
    hugo server -D
    ```
5. Go to web server link provided in output, usually [http://localhost:1313/](http://localhost:1313/) : 
    ```text {lineNos=false, hl_Lines=6, display="output"}
    ...
    Built in 72 ms
    Environment: "development"
    Serving pages from disk
    Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
    Web Server is available at http://localhost:1313/ (bind address 127.0.0.1) 
    Press Ctrl+C to stop
    ```
6. You should be able to preview your web page here. Also, this would be auto-updated every time you make changes to your markdown file and save it :
    ```text {lineNos=false, display="output"}
    ...
    Change detected, rebuilding site (#36).
    2025-10-06 13:43:53.971 +0100
    Source changed /code/20251106_publishing_using_hugo.md
    Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
    Total in 4 ms
    ```
    So, no need to run above command again and again.

## Step 3 : Pushing to Github
1. Create a [new repository](https://github.com/new) on github.
2. Copy `<github-project-url>` from above created project : e.g https://github.com/gauthamchettiar/gauthamchettiar.github.io
3. Run below set of commands from your hugo blog directory created in above steps : 
    ```bash
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin <github-project-url> # replace with copied URL
    git push -u origin main
    ```

## Step 4 : Publishing using Cloudflare Pages
<!-- > Since this gets updated pretty much all the time, there is no guarantee that this will continue to work in future. For latest instruction check [official docs](). -->

1. Signup for [Cloudflare Pages](https://dash.cloudflare.com/sign-up/workers-and-pages) account.
2. Search for "Workers & Pages", and go to that page : 
    ![Cloudflare - Workers & Pages Seach](/code/20251106_publishing_using_hugo/cf_workers_and_pages.png)
    As of writing this post, this is at *Compute (Workers) > Workers & Pages*
3. Click on "Create Application" :
    ![Cloudflare - Create Application](/code/20251106_publishing_using_hugo/cf_create_application.png)
4. Select repository : ![Cloudflare - Deploy 1](/code/20251106_publishing_using_hugo/cf_hugo_deploy_1.png)
    - Link your github account to cloudflare pages using "Add Account", then 
    - Choose the repository where hugo blog is pushed to, and
    - Click on "Begin Setup".
5. Setup builds and deployments: ![Cloudflare - Deploy 2](/code/20251106_publishing_using_hugo/cf_hugo_deploy_2.png)
   - Choose a name for your project, this will be deployed as:  
        `https://<project-name>.pages.dev`
   - Choose "Production branch" as "master", then
   - Choose "Framework Preset" as "Hugo", and
   - Click on "Save and Deploy"
6. Your deployment would finish and you would be given a link where your app is deployed : ![Cloudflare - Deploy 3](/code/20251106_publishing_using_hugo/cf_hugo_deploy_3.png)
7. This is a live link that you can immediately start sharing with everyone. 

## Step 5 (Optional) : Setting up custom domain
While this is not required, it's nice to have a permanent address on internet.

1. Come up with a good available domain name for your blog (*believe me this is the hardest part of all*).
2. Buy a domain on [GoDaddy](https://www.godaddy.com/en-uk), or from any registrar where you find [registration and renewal options to be cheapest](https://tld-list.com/).
3. Go back to cloudflare "Workers & Pages" > "Custom Domain" > "Set up a custom domain" : ![Cloudflare - Custom Domain 1](/code/20251106_publishing_using_hugo/cf_custom_domain.png)
4. Add a domain, it could include a subdomain (*blog.yourdomain.com*) if you wish:  ![Cloudflare - Custom Domain 2](/code/20251106_publishing_using_hugo/cf_custom_domain_2.png)
5. Once you click on "Activate domain" it would add your record to it's DNS. 
6. In order for cloudflare to manage DNS records, you need to [add nameservers](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#update-your-nameservers) displayed in Cloudflare to your domain registrar (GoDaddy in this case) : ![GoDaddy Nameserver Setup](/code/20251106_publishing_using_hugo/godaddy_nameserver_setup.png)
7. It could take upto 24 hours for entire thing to be up and running!  


Since, websites keep getting updated pretty often. Steps and Screenshots provided here might change in future. 

I will try my best to keep this post updated regularly, for future visitors ==`16th Dec 2025`== is the last day I verified that all steps work properly.

Feel free to [contact](/contact/) me in any of the socials provided in case you could not get any of the above steps to work. 