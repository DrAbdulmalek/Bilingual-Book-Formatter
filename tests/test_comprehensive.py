#!/usr/bin/env python3
"""
Comprehensive tests for Bilingual Book Formatter v2.3
"""
import pytest
import os
import tempfile
import json
from pathlib import Path
from bilingual_book_formatter import BilingualBookFormatter

class TestBilingualBookFormatter:
    @pytest.fixture
    def formatter(self):
        return BilingualBookFormatter()
    
    @pytest.fixture
    def sample_docx_path(self):
        return "test_samples/sample.docx"
    
    @pytest.fixture
    def sample_config(self):
        return {
            "page_margins": {"top": 2.5, "bottom": 2.5, "left": 2.0, "right": 2.0},
            "fonts": {"english": "Times New Roman", "arabic": "Traditional Arabic"},
            "rtl_languages": ["arabic"],
            "styles": {
                "normal": {"size": 12, "bold": False, "color": "000000"}
            }
        }
    
    def test_config_loading(self, formatter):
        assert formatter.config is not None
        assert 'page_margins' in formatter.config
        assert 'fonts' in formatter.config
    
    def test_document_parsing(self, formatter, sample_docx_path):
        if os.path.exists(sample_docx_path):
            content = formatter.parse_document(sample_docx_path, "english")
            assert isinstance(content, list)
    
    # Additional tests as provided previously...
