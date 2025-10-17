+++
title = '👨🏼‍🎨 Mods I made to Hugo Bear theme'
date = '2025-10-05T00:00:00+00:00'
description = ""
tags = ["blogging"]
draft = true
+++

A running log of all mods I made to [hugo-bearblog theme](https://github.com/janraasch/hugo-bearblog) to make the page looks the way I want. *Honestly, this is more of a test-bed to check if all my changes are working fine 😆*

## Shortcodes

### Wide Table
This is how default table in this theme looks like - 
| Generic | Markdown | Table  |
|---------|----------|--------|
| Boring  | to look  | at     |


And this is how wide-table shortcode looks like - 

{{< wide-table >}}
| Normal  | Markdown   | Table  | But         | Wider  |
|---------|------------|--------|-------------|--------|
| This is | responsive | too    |             |        |
|         |            | Try    | resizing    | window |

{{< /wide-table >}}