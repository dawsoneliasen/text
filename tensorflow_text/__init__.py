# coding=utf-8
# Copyright 2021 TF.Text Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Various tensorflow ops related to text-processing."""
from tensorflow.python.util.all_util import remove_undocumented

# pylint: disable=wildcard-import
from tensorflow_text.python import keras
from tensorflow_text.python import metrics
from tensorflow_text.python.ops import *


# Public symbols in the "tensorflow_text" package.  Symbols are sorted in
# increasing order of their lowercase version.
_allowed_symbols = [
    "BertTokenizer",
    "Detokenizer",
    "FirstNItemSelector",
    "HubModuleSplitter",
    "HubModuleTokenizer",
    "MaskValuesChooser",
    "RandomItemSelector",
    "Reduction",
    "RegexSplitter",
    "RoundRobinTrimmer",
    "SentencepieceTokenizer",
    "SplitMergeFromLogitsTokenizer",
    "SplitMergeTokenizer",
    "Splitter",
    "SplitterWithOffsets",
    "StateBasedSentenceBreaker",
    "Tokenizer",
    "TokenizerWithOffsets",
    "UnicodeCharTokenizer",
    "UnicodeScriptTokenizer",
    "WaterfallTrimmer",
    "WhitespaceTokenizer",
    "WordShape",
    "WordpieceTokenizer",
    "case_fold_utf8",
    "coerce_to_structurally_valid_utf8",
    "combine_segments",
    "find_source_offsets",
    "gather_with_default",
    "greedy_constrained_sequence",
    "keras",
    "mask_language_model",
    "max_spanning_tree",
    "max_spanning_tree_gradient",
    "metrics",
    "ngrams",
    "normalize_utf8",
    "normalize_utf8_with_offsets_map",
    "pad_along_dimension",
    "pad_model_inputs",
    "regex_split",
    "regex_split_with_offsets",
    "sentence_fragments",
    "sliding_window",
    "span_alignment",
    "span_overlaps",
    "viterbi_constrained_sequence",
    "wordshape",
]

remove_undocumented(__name__, _allowed_symbols)
__version__ = "2.5.0"
