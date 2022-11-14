FROM node:16
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 6688

CMD [ "node", "index.js" ]