FROM node:16

WORKDIR /api

COPY package*.json ./

RUN yarn install

COPY . .

CMD [ "node", "index.js" ]
