cd /mnt/data
rm -rf persona_mining_v1_git
unzip persona_mining_v1.zip -d persona_mining_v1_git
cd persona_mining_v1_git

git init
gh repo create taipei49314/persona-mining-v1 --public --source=. --remote=origin --push --default-branch=main