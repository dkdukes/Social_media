# Social Media App Project
## Features
### User Registration and Authentication
- Users can create new accounts and log in to the application.
- Passwords are securely stored using hashing techniques.
- User authentication ensures that only authorized users can access protected features.
### User Profiles
- Each user has a profile that displays their information and activities
- Users can upload a profile picture and update their personal details.
- The profile page shows the user's posts, followers, and following information.
### News Feed
- Users can view a personalized news feed that displays posts from users they follow.
- The feed is dynamically updated to show the latest posts from followed users.
- Users can like, comment on, and share posts directly from the feed.
### Creating and Editing Posts
- Users can create new posts with text, images, or videos.
- They can edit or delete their own posts.
- The posts can be tagged with relevant hashtags for easy discovery.
### Commenting and Interactions
- Users can comment on posts and engage in discussions.
- They can like or dislike posts and comments to express their opinion.
- Notifications are sent to users when someone interacts with their posts or comments.
### User Search and Discovery
- Users can search for other users based on their usernames or profile information.
- They can follow or unfollow other users to customize their news feed.
- Trending posts, popular users, or recommended profiles can be featured for user discovery.
## End Points
### Profile Endpoints
- GET /api/profiles/{user_id}/: Retrieve the profile of a specific user.
- PUT /api/profiles/{user_id}/: Update the profile of a specific user.
### Post Endpoints
- GET /api/posts/: Retrieve a list of all posts.
- GET /api/posts/{post_id}/: Retrieve details of a specific post.
- POST /api/posts/: Create a new post.
- PUT /api/posts/{post_id}/: Update a specific post.
- DELETE /api/posts/{post_id}/: Delete a specific post.
### Comment Endpoints
- GET /api/posts/{post_id}/comments/: Retrieve all comments for a specific post.
- POST /api/posts/{post_id}/comments/: Add a new comment to a specific post.
- PUT /api/comments/{comment_id}/: Update a specific comment.
- DELETE /api/comments/{comment_id}/: Delete a specific comment.
### Like Endpoints
- POST /api/posts/{post_id}/like/: Like a specific post.
- POST /api/comments/{comment_id}/like/: Like a specific comment.
- DELETE /api/posts/{post_id}/like/: Remove a like from a specific post.
- DELETE /api/comments/{comment_id}/like/: Remove a like from a specific comment.
### Follow Endpoints
- POST /api/users/{user_id}/follow/: Follow a specific user.
- DELETE /api/users/{user_id}/follow/: Unfollow a specific user.
### Search Endpoints
- GET /api/search/users/?query={search_query}: Search for users based on a search query.