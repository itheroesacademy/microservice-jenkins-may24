
FROM node:14-alpine
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
EXPOSE 8090
CMD ["npm", "start"]
