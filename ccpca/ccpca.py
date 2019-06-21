#  Because pybind11 cannot generate default parameters well, this code is to set them

import ccpca_cpp


class CCPCA(ccpca_cpp.CCPCA):
    """ccPCA. A variation of cPCA for contrasting the target cluster to the
    others

    Parameters
    ----------
    n_components: int, optional, (default=2)
        A number of componentes to take.
    standardize: boo, optional, (default=True)
        Whether standardize input matrices or not.
    Attributes
    ----------
    None.
    ----------
    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from sklearn import datasets

    >>> from ccpca import CCPCA

    >>> dataset = datasets.load_iris()
    >>> X = dataset.data
    >>> y = dataset.target

    >>> # get dimensionality reduction result with the best alpha
    >>> ccpca = CCPCA()
    >>> ccpca.fit_with_best_alpha(X[y == 0], X[y != 0], var_thres_ratio=0.5)
    >>> X_new = ccpca.transform(X)

    >>> # plot result
    >>> plt.figure()
    >>> colors = ['navy', 'turquoise', 'darkorange']
    >>> lw = 2
    >>> for color, i, target_name in zip(colors, [0, 1, 2], [0, 1, 2]):
    ...     plt.scatter(
    ...         X_new[y == i, 0],
    ...         X_new[y == i, 1],
    ...         color=color,
    ...         alpha=.8,
    ...         lw=lw,
    ...         label=target_name)
    >>> plt.legend(loc='best', shadow=False, scatterpoints=1)
    >>> plt.title('cPCA of IRIS dataset with automatic alpha =' +
    ...       str(dc.get_best_alpha()))
    >>> plt.show()
    Notes
    -----
    python version of fit_transform_with_best_alpha does not work properly
    right now.
    """

    def __init__(self, n_components=2, standardize=True):
        super().__init__(n_components, standardize)

    def transform(self, X):
        """Obtaining transformed result Y with X and current cPCs.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Testing data, where n_samples is the number of samples and
            n_features is the number of features. n_features must be the same
            size with the traiding data's features used for partial_fit.
        Returns
        -------
        Y : array-like, shape (n_samples, n_components)
            Returns the transformed (or projected) result.
        """
        return super().transform(X)

    def fit_transform_with_best_alpha(self,
                                      K,
                                      R,
                                      var_thres_ratio,
                                      parallel=True,
                                      n_alphas=40,
                                      max_log_alpha=3.0,
                                      keep_reports=False):
        """TODO: some bug, seems fit_transform does not work properly

        Find the best contrast parameter alpha first, fit using cPCA
        with the best alpha, and then transform a matrix concatenating K and R
        with cPCs. For cPCA, a matrix E concatenating K and R willbe used as a
        foreground dataset and R will be used as a background dataset.
        Parameters
        ----------
        K: array-like, shape(n_samples, n_components)
            A target cluster.
        R: array of array-like, n_groups x shape(n_samples, n_components)
            Background datasets.
        var_thres_ratio: float
            Ratio threshold of variance of A to keep.
        parallel: bool, optional, (default=True)
            If True, multithread implemented in C++ will be used for
            calculation.
        n_alphas: int, optional, (default=40)
            A number of alphas to check to find the best one.
        max_log_alpha: float, optional, (default=3.0)
            10.0 ** max_log_alpha is the maximum value of alpha will be used.
        Returns
        -------
        None
        """
        return super().fit_transform_with_best_alpha(
            K, R, var_thres_ratio, parallel, n_alphas, max_log_alpha,
            keep_reports)

    def fit_with_best_alpha(self,
                            K,
                            R,
                            var_thres_ratio,
                            parallel=True,
                            n_alphas=40,
                            max_log_alpha=3.0,
                            keep_reports=False):
        """Find the best contrast parameter alpha first and then fit using cPCA
        with the best alphaself. For cPCA, a matrix E concatenating K and R will
        be used as a foreground dataset and R will be used as a background
        dataset.
        Parameters
        ----------
        K: array-like, shape(n_samples, n_components)
            A target cluster.
        R: array of array-like, n_groups x shape(n_samples, n_components)
            Background datasets.
        var_thres_ratio: float
            Ratio threshold of variance of A to keep.
        parallel: bool, optional, (default=True)
            If True, multithread implemented in C++ will be used for
            calculation.
        n_alphas: int, optional, (default=40)
            A number of alphas to check to find the best one.
        max_log_alpha: float, optional, (default=3.0)
            10.0 ** max_log_alpha is the maximum value of alpha will be used.
        Returns
        -------
        None
        """
        super().fit_with_best_alpha(K, R, var_thres_ratio, parallel, n_alphas,
                                    max_log_alpha, keep_reports)

    def best_alpha(self,
                   K,
                   R,
                   var_thres_ratio,
                   parallel=True,
                   n_alphas=40,
                   max_log_alpha=3.0,
                   keep_reports=False):
        """Finds the best contrast parameter alpha which has high discrepancy
        score between the dimensionality reduced K and the dimensionality
        reduced R while keeping the variance of K with the ratio threshold
        var_thres_ratio.
        For cPCA, a matrix E concatenating K and R will be used as a foreground
        dataset and R will be used as a background dataset.
        Parameters
        ----------
        K: array-like, shape(n_samples, n_components)
            A target cluster.
        R: array of array-like, n_groups x shape(n_samples, n_components)
            Background datasets.
        var_thres_ratio: float
            Ratio threshold of variance of A to keep.
        parallel: bool, optional, (default=True)
            If True, multithread implemented in C++ will be used for
            calculation.
        n_alphas: int, optional, (default=40)
            A number of alphas to check to find the best one.
        max_log_alpha: float, optional, (default=3.0)
            10.0 ** max_log_alpha is the maximum value of alpha will be used.
        Returns
        -------
        best_alpha: float
            The found best alpha.
        """
        return super().best_alpha(K, R, var_thres_ratio, parallel, n_alphas,
                                  max_log_alpha, keep_reports)

    def get_feat_contribs(self):
        """Returns feature contributions from current cPCA result. The
        feature contributions are the same value with the first cPC loading.
        Parameters
        ----------
        None
        Returns
        -------
        feat_contribs: array-like, shape(n_features, 1)
            Feature contributions.
        """
        return super().get_feat_contribs()

    def get_scaled_feat_contribs(self):
        """Returns scaled feature contributions from current cPCA result.
        Scaled feature contributions are in the range from -1 to 1 by dividing
        each feature contribution by the maximum absolute value of the FCs
        (e.g., the original range from -0.1 to 0.5 will be changed to the range
        from -0.2 to 1.0)
        Parameters
        ----------
        None
        Returns
        -------
        feat_contribs: array-like, shape(n_features, 1)
            Feature contributions.
        """
        return super().get_scaled_feat_contribs()

    def get_first_component(self):
        """Returns the firsrt PC from current cPCA result.
        Parameters
        ----------
        None
        Returns
        -------
        pc: array, shape(n_features)
            The first principal component.
        """
        return super().get_feat_contribs()

    def get_best_alpha(self):
        """Returns best alpha found with best_alpha()
        Parameters
        ----------
        None
        -------
        best_alpha: float
            The found best alpha.
        """
        return super().get_best_alpha()

    def get_reports(self):
        return super().get_reports()
