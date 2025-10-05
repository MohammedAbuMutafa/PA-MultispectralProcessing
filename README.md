# PA-MultispectralProcessing

A comprehensive precision agriculture multispectral image processing service that handles drone-captured imagery for crop monitoring and analysis.

## Overview

PA-MultispectralProcessing is the core processing engine for the Precision Agriculture ecosystem. It processes multispectral drone imagery to generate vegetation indices, crop health analysis, and agricultural insights using advanced computer vision and remote sensing techniques.

## Features

### Multispectral Image Processing
- **NDVI Calculation**: Normalized Difference Vegetation Index computation
- **Vegetation Indices**: Multiple spectral indices for crop health assessment
- **Image Registration**: Alignment and calibration of multispectral bands
- **Data Fusion**: Integration of RGB and multispectral imagery

### Processing Modules
- **NewImageProcessor**: Main processing pipeline for incoming drone imagery
- **Modular Architecture**: Extensible processing modules for different analysis types
- **Batch Processing**: Efficient handling of large image datasets
- **Real-time Processing**: Live processing capabilities for drone feeds

### Data Management
- **DTOs**: Structured data transfer objects for consistent data flow
- **Exception Handling**: Comprehensive error management and logging
- **Configuration Management**: Environment-based configuration system
- **Logging**: Detailed processing logs with timestamps

## Project Structure

```
PA-MultispectralProcessing/
├── Modules/                    # Processing modules
│   ├── NDVIProcessor.py       # NDVI calculation module
│   ├── ImageProcessor.py      # Core image processing
│   ├── SpectralAnalyzer.py    # Spectral analysis tools
│   └── [other modules]        # Additional processing modules
├── Processors/                # Main processing pipelines
│   └── NewImageProcessor.py   # Primary image processing service
├── dto/                       # Data Transfer Objects
│   ├── ImageDto.py           # Image data structure
│   ├── ProcessingDto.py      # Processing parameters
│   └── [other DTOs]          # Additional data structures
├── Enums/                     # Enumeration definitions
│   ├── ProcessingType.py     # Processing type enumerations
│   └── ImageFormat.py        # Supported image formats
├── Exceptions/                # Custom exception classes
│   └── ImageDtoMapException.py # Image processing exceptions
├── Helpers/                   # Utility functions
│   └── ImageHelper.py        # Image manipulation utilities
├── main.py                   # Application entry point
├── Dockerfile               # Container configuration
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technology Stack

### Core Technologies
- **Python 3.11+**: Primary programming language
- **Rasterio**: Geospatial raster data processing
- **NumPy**: Numerical computations and array operations
- **Matplotlib**: Data visualization and plotting
- **TIFFFile**: TIFF image format handling

### Infrastructure
- **Docker**: Containerized deployment
- **RabbitMQ**: Message queuing for distributed processing
- **Flask**: Web service framework
- **Python-dotenv**: Environment configuration management

### Image Processing
- **OpenCV**: Computer vision and image processing
- **PIL/Pillow**: Python Imaging Library
- **Scikit-image**: Image processing algorithms

## Installation and Setup

### Prerequisites
- Python 3.11 or higher
- Docker (optional, for containerized deployment)
- RabbitMQ server (for message queuing)

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MohammedAbuMutafa/PA-MultispectralProcessing.git
   cd PA-MultispectralProcessing
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   Create a `.env` file with the following variables:
   ```env
   VERSION=1.0.0
   SESSION_KEY=your_session_key
   
   # Directory paths for multispectral bands
   GREEN_DIR=/path/to/green/band/images
   NIR_DIR=/path/to/nir/band/images
   RED_DIR=/path/to/red/band/images
   RED_EDGE_DIR=/path/to/red_edge/band/images
   
   # Data directories
   DATA_DIR=/path/to/input/data
   OUTPUT_BASE_PATH=/path/to/output/directory
   
   # RabbitMQ configuration
   RMQ_HOST=localhost
   RMQ_INCOMING_NAME=incoming_queue
   RMQ_OUTGOING_NAME=outgoing_queue
   
   # API endpoints
   API_BASE=http://localhost:5000
   NEW_SESSION_ENDPOINT=/api/session/new
   NEW_IMAGE_ENDPOINT=/api/image/process
   
   # Debug mode
   DEBUG_MODE=FALSE
   ```

### Running the Application

#### Local Development
```bash
python main.py
```

#### Docker Deployment
```bash
docker build -t pa-multispectral-processing .
docker run -d --name pa-processor \
  -e VERSION=1.0.0 \
  -v /path/to/data:/app/data \
  pa-multispectral-processing
```

## Usage

### Processing Multispectral Images

1. **Configure Input Directories**: Set up the multispectral band directories in your `.env` file
2. **Start the Service**: Run the main application
3. **Submit Images**: Send multispectral images through the API or message queue
4. **Monitor Processing**: Check logs for processing status and results

### API Endpoints

- **POST /api/session/new**: Create a new processing session
- **POST /api/image/process**: Submit image for processing
- **GET /api/status**: Check processing service status

### Message Queue Integration

The service integrates with RabbitMQ for distributed processing:
- **Incoming Queue**: Receives image processing requests
- **Outgoing Queue**: Sends processing results and notifications

## Processing Pipeline

1. **Image Reception**: Receive multispectral drone imagery
2. **Preprocessing**: Image calibration and alignment
3. **Spectral Analysis**: Calculate vegetation indices (NDVI, etc.)
4. **Data Fusion**: Combine multispectral and RGB data
5. **Result Generation**: Generate analysis reports and visualizations
6. **Output Delivery**: Send results via API or message queue

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VERSION` | Application version | Yes |
| `SESSION_KEY` | Session management key | Yes |
| `GREEN_DIR` | Green band image directory | Yes |
| `NIR_DIR` | NIR band image directory | Yes |
| `RED_DIR` | Red band image directory | Yes |
| `RED_EDGE_DIR` | Red edge band image directory | Yes |
| `DATA_DIR` | Input data directory | Yes |
| `OUTPUT_BASE_PATH` | Output directory path | Yes |
| `RMQ_HOST` | RabbitMQ host address | Yes |
| `RMQ_INCOMING_NAME` | Incoming queue name | Yes |
| `RMQ_OUTGOING_NAME` | Outgoing queue name | Yes |
| `API_BASE` | API base URL | Yes |
| `DEBUG_MODE` | Enable debug logging | No |

## Logging

The application generates detailed logs with:
- Processing timestamps
- Error tracking
- Performance metrics
- Debug information (when enabled)

Logs are stored in the `logs/` directory with timestamped filenames.

## Integration

### With Other PA Components
- **PA-Backend**: Receives processing requests and results
- **PA-Web**: Provides user interface for processing management
- **PA-Utils**: Utilizes utility functions for image processing
- **PA-Components**: Shares processing modules and utilities

### Message Queue Integration
- **RabbitMQ**: Primary message broker for distributed processing
- **Queue Management**: Automatic queue creation and management
- **Error Handling**: Robust error handling and retry mechanisms

## Development

### Adding New Processing Modules

1. Create a new module in the `Modules/` directory
2. Implement the required processing interface
3. Add configuration options to environment variables
4. Update the main processor to include the new module

### Testing

Run the test suite:
```bash
python -m pytest tests/
```

### Code Style

Follow PEP 8 guidelines and use type hints for better code documentation.

## Troubleshooting

### Common Issues

1. **Missing Environment Variables**: Ensure all required variables are set in `.env`
2. **Directory Permissions**: Check read/write permissions for data directories
3. **RabbitMQ Connection**: Verify RabbitMQ server is running and accessible
4. **Memory Issues**: Large images may require increased memory allocation

### Debug Mode

Enable debug mode by setting `DEBUG_MODE=TRUE` in your `.env` file for detailed logging.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is part of the Precision Agriculture ecosystem and is developed for research and educational purposes.

## Support

For issues and questions:
- Create an issue in the repository
- Check the logs for error details
- Review the configuration setup

---

*Part of the Precision Agriculture ecosystem - Bridging technology and farming for sustainable agriculture*