FROM node:18.18.0

WORKDIR /app/frontend

RUN sh -c "$(curl -L https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t robbyrussell \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/rupa/z/

RUN curl -fsSL https://get.pnpm.io/install.sh | bash

EXPOSE 5173

CMD [ "/bin/zsh"]
