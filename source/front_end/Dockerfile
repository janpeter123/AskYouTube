# Use official Node.js image as base
FROM node:latest

# Set working directory
WORKDIR /app

# Copy the entire project directory to the working directory
COPY . .

# Install dependencies
RUN npm install

# Expose the port Next.js runs on (default is 3000)
EXPOSE 3000

# Command to run the production server
CMD ["npm", "run","dev"]