# Blog Application

This repository contains the source code for a blog application built with Django. The project includes core blog features, such as creating, displaying, and managing blog posts, as well as advanced functionalities like SEO optimization, pagination, comments, and full-text search.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)

## Project Overview

This is a Django-based blog application where users can:

- **Create, edit, and delete blog posts.**
- **Comment on blog posts** using a custom comment system.
- **Search for posts** using full-text search.
- **Filter posts by tags** and view similar posts.
- **Send recommendations by email**.
- **Paginate the post list** to improve user experience.

The project also includes SEO-friendly URLs, email functionality, and the ability to handle complex content types using custom template tags and filters.

## Features

### Core Features
- **Post Creation & Management**: Users can create and manage blog posts, including adding metadata like publication date and post status.
- **Comment System**: Users can leave comments on blog posts using a model-based form.
- **Pagination**: The post list view includes pagination to handle large amounts of content efficiently.

### Advanced Features
- **SEO Optimization**: Custom URLs and canonical tags for posts to improve search engine rankings.
- **Class-Based Views**: Use of Django's class-based views to manage post listing and details.
- **Email Recommendations**: Users can recommend posts by email using Django's email functionality.
- **Full-Text Search**: Implemented using PostgreSQL and custom search ranking algorithms to improve content discovery.
- **Custom Template Tags & Filters**: Extended Django templates to support additional features like Markdown rendering and tag filtering.

## Technologies Used

- **Backend**: Django, Python
- **Database**: PostgreSQL (for full-text search)
- **Frontend**: HTML, CSS
- **Other**: Email functionality, Django class-based views, custom template tags and filters


