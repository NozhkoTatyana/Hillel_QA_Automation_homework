FROM python:3.14-slim AS builder
WORKDIR /lesson_30

# Install build dependencies into /root/.local
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.14-slim AS runtime
WORKDIR /lesson_30

# Create non-root user
RUN useradd -m -u 1000 appuser

# Copy dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code and ensure proper ownership
COPY . .
RUN rm -f test_db.log && chown -R appuser:appuser /lesson_30

# Set PATH to include user site-packages
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

CMD ["pytest"]
