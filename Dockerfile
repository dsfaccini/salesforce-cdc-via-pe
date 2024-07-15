FROM python:3.6-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD salesforce_platform_events.py /app
ADD .env /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir asyncio aiosfstream python-dotenv

# Make port 80 available to the world outside this container
# EXPOSE 80

# Run salesforce_platform_events.py when the container launches
CMD ["python", "salesforce_platform_events.py"]

# docker build -t sf_pe:1.0.0 .

# docker run -it --rm sf_pe:1.0.0