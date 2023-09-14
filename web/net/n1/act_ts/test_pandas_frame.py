#
#
#
import pandas as pd
import pytest
import pprint as pp
import logging
LOG = logging.getLogger(__name__)


#
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
# https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-and-then-filling-it
#

class PandaRoutines:

    @staticmethod
    def frame_info(a_dat_frame):
        dct={
            'shape': str(a_dat_frame.shape),
            'index': str(a_dat_frame.index),
            'columns': str(a_dat_frame.columns),
        }
        LOG.info(str(dct))



# Initilize a dataframe:

@pytest.mark.skip
class TestPandasFrame:

    nd1 = {
        "child1": {
            "name": "Emil",
            "year": 2004
        },
        "child2": {
            "name": "Tobias",
            "year": 2007
        },
        "child3": {
            "name": "Linus",
            "year": 2011
        }
    }

    nd2 = {
        'text_raw':'',
        'text_category':'',
        'text_page_number':'',
        'word_list':[
            {'raw': 'one', 'lemma': 'one_lemma'},
            {'raw': 'two', 'lemma': 'two_lemma'},
        ],
        'phrase_frame':[
            {'raw': 'one', 'lemma': 'one_lemma'},
            {'raw': 'two', 'lemma': 'two_lemma'},
        ],
    }

    df1 = pd.DataFrame(nd1)
    df2 = pd.DataFrame(columns=['name', 'text'])
    df3 = pd.DataFrame(nd2)

    df21 = pd.DataFrame(nd1)

    dfg1 = pd.DataFrame({'idx': [1, 2, 3], 'dfs': [df1, df2, df3]})

    df = dfg1

    @pytest.mark.order(1)
    def test_pandas_frame_i1_dat_frame(self, act_config):
        LOG.info(" act_config ")
        LOG.info(pp.pformat(str(act_config)))

        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)

    @pytest.mark.order(2)
    def test_pandas_frame_i2_dat_frame(self, act_config):

        LOG.info("\n")
        LOG.info(self.df)
        LOG.info(self.df.shape)
        LOG.info(self.df.columns)
        LOG.info(self.df.index)

        LOG.info(self.df.loc[1])
        LOG.info(self.df.loc[2])




@pytest.mark.skip
class TestPandasFrameObject:

    nd1 = {
        'text_raw':'all play no play make jakes dump',
        'text_category':'sports',
        'text_page_number':'1234',
        'word_list':[
            {'raw': 'one', 'lemma': 'one_lemma'},
            {'raw': 'two', 'lemma': 'two_lemma'},
        ],
        'phrase_list':[
            {'raw': 'one', 'lemma': 'one_lemma'},
            {'raw': 'two', 'lemma': 'two_lemma'},
        ],
    }

    df1 = pd.DataFrame(nd1)

    df = df1

    @pytest.mark.order(21)
    def test_pandas_frame_group_g21_json_decoder(self, act_config):

        LOG.info(self.df)
        LOG.info(self.df.shape)
        LOG.info(self.df.columns)
        LOG.info(self.df.index)

    @pytest.mark.order(21)
    def test_pandas_frame_group_g22(self, act_config):

        LOG.info(self.df)
        LOG.info(self.df.shape)
        LOG.info(self.df.columns)
        LOG.info(self.df.index)

        LOG.info( self.df['text_raw'] )
        LOG.info( self.df['text_category'] )
        LOG.info( self.df['text_page_number'] )
        LOG.info(self.df['word_list'])
        LOG.info(self.df['phrase_list'])



    @pytest.mark.order(21)
    def test_pandas_frame_group_g23(self, act_config):

        LOG.info(self.df)
        LOG.info(self.df.shape)
        LOG.info(self.df.columns)
        LOG.info(self.df.index)



@pytest.mark.skip
class TestPandasFrameFromScratch:

    # @pytest.mark.skip
    @pytest.mark.order(21)
    def test_pandas_frame_from_scratch_s51(self, act_config):

        #df1 = pd.DataFrame(columns=['uid','raw'])
        df1 = pd.DataFrame(columns=['raw'])
        LOG.info(df1.shape)
        LOG.info(df1.columns)
        LOG.info(df1.index)
        LOG.info(len(df1.index))

        #df1.iloc[len(df1.index)]
        #df1.iloc[len(df1.index)] = ['101', 'Amy']
        #df1.iloc[len(df1.index)] =
        #LOG.info(df1.shape)
        #LOG.info(type(df1.index))
        #df1.append( {'raw': 'Amy'} )
        # pass

    @pytest.mark.order(52)
    def test_pandas_frame_from_scratch_s52(self, act_config):

        dict = {'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
               'Maths': [87, 91, 97, 95],
               'Science': [83, 99, 84, 76]
               }

        df = pd.DataFrame(dict)

        LOG.info(df)

        df.loc[len(df.index)] = ['Amy', 89, 93]
        LOG.info


@pytest.mark.skip
class TestDocFrame:
    cf = pd.DataFrame({})

    @pytest.mark.order(21)
    def test_doc_frame_group_g22(self, act_config):
        pass


@pytest.mark.skip
class TestCorpusFrame:
    cf = pd.DataFrame({})


    nd1 = {
        'text_raw':'',
        'text_category':'',
        'text_page_number':'',
        'word_list':[
            {'raw': 'one', 'lemma': 'one_lemma'},
            {'raw': 'two', 'lemma': 'two_lemma'},
        ],
        'phrase_frame':[
            {'raw': 'one', 'lemma': 'one_lemma'},
            {'raw': 'two', 'lemma': 'two_lemma'},
        ],
    }

    nd2 = {
        "child1": {
            "name": "Emil",
            "year": 2004
        },
        "child2": {
            "name": "Tobias",
            "year": 2007
        },
        "child3": {
            "name": "Linus",
            "year": 2011
        }
    }

    df1 = pd.DataFrame(nd1)
    df2 = pd.DataFrame(columns=['name', 'text'])
    df3 = pd.DataFrame(nd2)

    df21 = pd.DataFrame(nd1)

    dfg1 = pd.DataFrame({'idx': [1, 2, 3], 'dfs': [df1, df2, df3]})

    df = dfg1


@pytest.mark.skip
class TestPandasDictRow:

    # nested dictionary
    nd1 = {
        "child1": {
            "name": "Emil",
            "year": 2004
        },
        "child2": {
            "name": "Tobias",
            "year": 2007
        },
        "child3": {
            "name": "Linus",
            "year": 2011
        }
    }

    df1 = pd.DataFrame(nd1)

    @pytest.mark.order(1)
    def test_pandas_row4dict_l1(self, act_config):
        LOG.info(" act_config ")
        LOG.info(pp.pformat(str(act_config)))

        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)


@pytest.mark.skip
class TestPandasListRow:

    lst1 = [['a','b','c'],['e','f','g']]

    df1 = pd.DataFrame(lst1 , columns=['x','y','z'])

    @pytest.mark.order(1)
    def test_pandas_row4list_l1(self, act_config):
        LOG.info(" act_config ")
        LOG.info(pp.pformat(str(act_config)))

        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)


@pytest.mark.skip
class TestPandasDictCol:

    # nested dictionary
    nd1 = {
        "child1": {
            "uid": 1,
            "year": 2004
        },
        "child2": {
            "uid": 2,
            "year": 2007
        },
        "child3": {
            "uid": 3,
            "year": 2011
        }
    }

    df1 = pd.DataFrame(nd1)


    @pytest.mark.order(3)
    def test_pandas_dict_col_c1_new(self, act_config):

        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)

        self.df1["child4"] = self.df1["child3"]
        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)


    @pytest.mark.order(4)
    def test_pandas_dict_col_c2_del(self, act_config):
        # https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe

        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)

        self.df2 = self.df1.drop('child3', axis=1)

        LOG.info(self.df2)
        LOG.info(self.df2.shape)
        LOG.info(self.df2.columns)
        LOG.info(self.df2.index)


    @pytest.mark.order(21)
    def test_pandas_dict_col_c3_update(self, act_config):

        LOG.info(self.df1)
        LOG.info(self.df1.shape)
        LOG.info(self.df1.columns)
        LOG.info(self.df1.index)

