# Useful Git Commands

## Configuration

- Configure user information for all local repositories:
  `
  git config --global user.name "Your_Name"
  git config --global user.email "youremail@email.com"
  `

## Repository Initialization

- Initialize a new Git repository:
  `
  git init
  `
  
## Cloning

- Clone a repository:
  `
  git clone [repository_url]
  `

## Staging and Committing

- Add changes to the staging area:
  `
  git add [file]
  `
- Commit changes:
  `
  git commit -m "Commit message"
  `

## Branching

- Create a new branch:
  `
  git branch [branch_name]
  `
- Switch to a branch:
  `
  git checkout [branch_name]
  `
- Create and switch to a new branch:
  `
  git checkout -b [new_branch_name]
  `

## Merging

- Merge a branch into the current branch:
  `
  git merge [branch_name]
  `

## Remote Repositories

- Add a remote repository:
  `
  git remote add origin [remote_repository_url]
  `
- Push changes to a remote repository:
  `
  git push origin [branch_name]
  `

## Updating and Publishing

- Update local repository with changes from the remote repository:
  `
  git pull
  `
- Publish local changes to a remote repository:
  `
  git push
  `

## Logging and History

- Show commit history:
  `
  git log
  `

## Tagging

- Tag a specific commit:
  `
  git tag [tag_name] [commit_id]
  `

## Undoing Changes

- Discard changes in working directory:
  `
  git checkout -- [file]
  `
- Discard changes in the staging area:
  `
  git reset HEAD [file]
  `

## Miscellaneous

- Show the status of working directory and staging area:
  ``
  git status
  `
- Show the differences between commits, branches, etc.:
  `
  git diff
  `
